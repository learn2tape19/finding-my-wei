add_action('rest_api_init', function () {
    register_rest_route('tao/v1', '/subscribe', [
        'methods'  => 'POST',
        'callback' => 'tao_handle_subscribe',
        'permission_callback' => '__return_true',
        'args' => [
            'email' => [
                'required' => true,
                'type' => 'string',
                'sanitize_callback' => 'sanitize_email',
            ],
            'source' => [
                'required' => false,
                'type' => 'string',
                'sanitize_callback' => 'sanitize_text_field',
                'default' => 'unknown',
            ],
        ],
    ]);
});

function tao_handle_subscribe(WP_REST_Request $request) {
    if (!defined('TAO_BREVO_API_KEY')) {
        return new WP_REST_Response(
            ['status' => 'error', 'code' => 'config', 'message' => 'Subscription is temporarily unavailable.'],
            503
        );
    }

    $email  = $request->get_param('email');
    $source = $request->get_param('source');

    if (empty($email) || !is_email($email)) {
        return new WP_REST_Response(
            ['status' => 'error', 'code' => 'invalid_email', 'message' => 'Please enter a valid email address.'],
            400
        );
    }

    // Rate limit: simple transient-based per-IP throttle (5 attempts per 10 min).
    $ip_hash = hash('sha256', isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'unknown');
    $rate_key = 'tao_sub_rate_' . substr($ip_hash, 0, 12);
    $attempts = (int) get_transient($rate_key);
    if ($attempts >= 5) {
        return new WP_REST_Response(
            ['status' => 'error', 'code' => 'rate_limit', 'message' => 'Too many attempts. Please try again later.'],
            429
        );
    }
    set_transient($rate_key, $attempts + 1, 600);

    // Call Brevo double opt-in endpoint.
    $brevo_body = wp_json_encode([
        'email'          => $email,
        'includeListIds' => [64],
        'templateId'     => 37,
        'redirectionUrl' => 'https://taoclinicaltouch.com/subscription-confirmed/',
    ]);

    $response = wp_remote_post('https://api.brevo.com/v3/contacts/doubleOptinConfirmation', [
        'headers' => [
            'accept'       => 'application/json',
            'content-type' => 'application/json',
            'api-key'      => TAO_BREVO_API_KEY,
        ],
        'body'    => $brevo_body,
        'timeout' => 15,
    ]);

    if (is_wp_error($response)) {
        return new WP_REST_Response(
            ['status' => 'error', 'code' => 'network', 'message' => 'Something went wrong. Please try again.'],
            500
        );
    }

    $http_code   = wp_remote_retrieve_response_code($response);
    $body_raw    = wp_remote_retrieve_body($response);
    $body_parsed = json_decode($body_raw, true);

    if ($http_code === 201 || $http_code === 204) {
        return new WP_REST_Response(
            ['status' => 'success', 'code' => 'doi_sent', 'message' => 'Check your email to confirm your subscription.'],
            200
        );
    }

    if ($http_code === 400 && is_array($body_parsed) && isset($body_parsed['message'])) {
        if (stripos($body_parsed['message'], 'already exist') !== false) {
            return new WP_REST_Response(
                ['status' => 'success', 'code' => 'already_subscribed', 'message' => 'You may already be subscribed. Check your email for a confirmation link.'],
                200
            );
        }
    }

    return new WP_REST_Response(
        ['status' => 'error', 'code' => 'service', 'message' => 'Something went wrong. Please try again.'],
        500
    );
}
