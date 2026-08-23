/**
 * tao-publication-signup.js — v1.0.0
 * Canonical email subscription component for The Tao of Clinical Touch.
 * Build once. Verify once. Inject everywhere.
 *
 * Requires: server-side endpoint at /wp-json/tao/v1/subscribe
 * Analytics: dataLayer → GTM (no direct gtag calls)
 * PII: email address NEVER enters dataLayer/analytics
 */
(function () {
  'use strict';

  // ── Configuration ──────────────────────────────────────────────
  var CONFIG = {
    version: '1.0.0',
    endpoint: '/wp-json/tao/v1/subscribe',
    publication: 'tao_clinical_touch',
    // Set by injection context — default to 'unknown'
    source: 'unknown',
  };

  // ── Detect source from root element data attribute ─────────────
  var root = document.getElementById('tao-publication-signup');
  if (!root) return; // Guard: only run when the component root exists.
  CONFIG.source = root.getAttribute('data-signup-source') || CONFIG.source;

  // ── Analytics helper (dataLayer only, zero PII) ────────────────
  function pushEvent(eventName, extra) {
    window.dataLayer = window.dataLayer || [];
    var payload = {
      event: eventName,
      signup_source: CONFIG.source,
      component_version: CONFIG.version,
      page_path: window.location.pathname,
      publication: CONFIG.publication,
    };
    if (extra) {
      for (var k in extra) {
        if (extra.hasOwnProperty(k)) payload[k] = extra[k];
      }
    }
    window.dataLayer.push(payload);
  }

  // ── Styles (scoped under #tao-publication-signup) ──────────────
  var css = [
    '#tao-publication-signup {',
    '  max-width: 640px;',
    '  margin: 48px auto 0;',
    '  padding: 40px 32px 36px;',
    '  font-family: Georgia, "Times New Roman", serif;',
    '  color: #f5f0e8;',
    '  text-align: center;',
    '  border-top: 1px solid rgba(245, 240, 232, 0.25);',
    '  box-sizing: border-box;',
    '}',
    '#tao-publication-signup *, #tao-publication-signup *::before, #tao-publication-signup *::after {',
    '  box-sizing: border-box;',
    '}',
    '#tao-publication-signup .tao-signup-headline {',
    '  font-size: 1.25rem;',
    '  font-weight: 700;',
    '  margin: 0 0 6px;',
    '  color: #f5f0e8;',
    '  letter-spacing: 0.01em;',
    '}',
    '#tao-publication-signup .tao-signup-description {',
    '  font-size: 0.95rem;',
    '  line-height: 1.6;',
    '  color: #c8cfd6;',
    '  margin: 0 0 24px;',
    '  font-style: italic;',
    '}',
    '#tao-publication-signup .tao-signup-form {',
    '  display: flex;',
    '  gap: 10px;',
    '  justify-content: center;',
    '  align-items: flex-start;',
    '  flex-wrap: wrap;',
    '  margin: 0;',
    '}',
    '#tao-publication-signup .tao-signup-field-wrap {',
    '  position: relative;',
    '  flex: 1 1 260px;',
    '  max-width: 340px;',
    '}',
    '#tao-publication-signup .tao-signup-label {',
    '  position: absolute;',
    '  width: 1px; height: 1px;',
    '  padding: 0; margin: -1px;',
    '  overflow: hidden;',
    '  clip: rect(0,0,0,0);',
    '  border: 0;',
    '}',
    '#tao-publication-signup .tao-signup-input {',
    '  width: 100%;',
    '  padding: 11px 14px;',
    '  font-family: Georgia, "Times New Roman", serif;',
    '  font-size: 0.95rem;',
    '  color: #1a2a3a;',
    '  background: #fff;',
    '  border: 1px solid #a0aab4;',
    '  border-radius: 3px;',
    '  outline: none;',
    '  transition: border-color 0.2s;',
    '}',
    '#tao-publication-signup .tao-signup-input:focus {',
    '  border-color: #f5f0e8;',
    '}',
    '#tao-publication-signup .tao-signup-input.tao-input-error {',
    '  border-color: #c0392b;',
    '}',
    '#tao-publication-signup .tao-signup-input::placeholder {',
    '  color: #8a949e;',
    '  font-style: italic;',
    '}',
    '#tao-publication-signup .tao-signup-button {',
    '  padding: 11px 24px;',
    '  font-family: Georgia, "Times New Roman", serif;',
    '  font-size: 0.95rem;',
    '  font-weight: 700;',
    '  color: #1a2a3a;',
    '  background: #f5f0e8;',
    '  border: 1px solid #f5f0e8;',
    '  border-radius: 3px;',
    '  cursor: pointer;',
    '  white-space: nowrap;',
    '  transition: background 0.2s, opacity 0.2s;',
    '  line-height: 1.4;',
    '}',
    '#tao-publication-signup .tao-signup-button:hover {',
    '  background: #e8e0d4;',
    '}',
    '#tao-publication-signup .tao-signup-button:disabled {',
    '  opacity: 0.6;',
    '  cursor: not-allowed;',
    '}',
    '#tao-publication-signup .tao-signup-validation {',
    '  font-size: 0.82rem;',
    '  color: #e74c3c;',
    '  text-align: left;',
    '  margin: 4px 0 0;',
    '  min-height: 1.2em;',
    '}',
    '#tao-publication-signup .tao-signup-result {',
    '  margin-top: 20px;',
    '  padding: 16px 20px;',
    '  border-radius: 3px;',
    '  font-size: 0.95rem;',
    '  line-height: 1.5;',
    '}',
    '#tao-publication-signup .tao-signup-result.tao-result-success {',
    '  background: #eef6ee;',
    '  color: #1a5c2a;',
    '  border: 1px solid #b8dab8;',
    '}',
    '#tao-publication-signup .tao-signup-result.tao-result-error {',
    '  background: #fdf0ef;',
    '  color: #922;',
    '  border: 1px solid #e0bfbf;',
    '}',
    '#tao-publication-signup .tao-signup-footer {',
    '  font-size: 0.8rem;',
    '  color: #a0aab4;',
    '  margin-top: 16px;',
    '}',
    '#tao-publication-signup .tao-signup-success-headline {',
    '  font-size: 1.15rem;',
    '  font-weight: 700;',
    '  margin: 0 0 4px;',
    '}',
    '/* Success state: hide form, show result */',
    '#tao-publication-signup.tao-state-success .tao-signup-form,',
    '#tao-publication-signup.tao-state-success .tao-signup-footer {',
    '  display: none;',
    '}',
    '@media (max-width: 480px) {',
    '  #tao-publication-signup {',
    '    padding: 32px 20px 28px;',
    '  }',
    '  #tao-publication-signup .tao-signup-form {',
    '    flex-direction: column;',
    '    align-items: stretch;',
    '  }',
    '  #tao-publication-signup .tao-signup-field-wrap {',
    '    max-width: none;',
    '  }',
    '  #tao-publication-signup .tao-signup-button {',
    '    width: 100%;',
    '  }',
    '}',
  ].join('\n');

  var styleEl = document.createElement('style');
  styleEl.textContent = css;
  document.head.appendChild(styleEl);

  // ── HTML ───────────────────────────────────────────────────────
  root.innerHTML = [
    '<p class="tao-signup-headline">Stay in the conversation.</p>',
    '<p class="tao-signup-description">The Tao of Clinical Touch explores the neuroscience of permission, therapeutic alliance, and the conditions that allow skilled touch to matter.</p>',
    '<form class="tao-signup-form" novalidate>',
    '  <div class="tao-signup-field-wrap">',
    '    <label for="tao-signup-email" class="tao-signup-label">Email address</label>',
    '    <input id="tao-signup-email" class="tao-signup-input" type="email" name="email" placeholder="Your email address" autocomplete="email" required aria-describedby="tao-signup-validation">',
    '    <div id="tao-signup-validation" class="tao-signup-validation" aria-live="polite"></div>',
    '  </div>',
    '  <button type="submit" class="tao-signup-button">Receive New Issues</button>',
    '</form>',
    '<div class="tao-signup-result" role="status" aria-live="polite" style="display:none;"></div>',
    '<p class="tao-signup-footer">New essays and clinical reflections. No noise. Unsubscribe anytime.</p>',
  ].join('\n');

  // ── DOM references ─────────────────────────────────────────────
  var form = root.querySelector('.tao-signup-form');
  var input = root.querySelector('.tao-signup-input');
  var button = root.querySelector('.tao-signup-button');
  var validation = root.querySelector('.tao-signup-validation');
  var resultBox = root.querySelector('.tao-signup-result');

  // ── Email validation (matches WordPress is_email basics) ───────
  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // ── View event ─────────────────────────────────────────────────
  pushEvent('tao_email_signup_view');

  // ── Clear validation on input ──────────────────────────────────
  input.addEventListener('input', function () {
    input.classList.remove('tao-input-error');
    validation.textContent = '';
  });

  // ── Form submission ────────────────────────────────────────────
  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var email = input.value.trim();

    // Client-side validation — reject before network.
    if (!email || !isValidEmail(email)) {
      input.classList.add('tao-input-error');
      validation.textContent = 'Please enter a valid email address.';
      input.focus();
      return;
    }

    // Analytics: submit (no PII).
    pushEvent('tao_email_signup_submit');

    // Disable form during submission.
    button.disabled = true;
    button.textContent = 'Sending\u2026';
    resultBox.style.display = 'none';
    resultBox.className = 'tao-signup-result';

    // POST to server-side endpoint.
    var xhr = new XMLHttpRequest();
    xhr.open('POST', CONFIG.endpoint, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
      var data;
      try {
        data = JSON.parse(xhr.responseText);
      } catch (err) {
        data = { status: 'error', message: 'Something went wrong. Please try again.' };
      }

      if (data.status === 'success') {
        // Success state.
        root.classList.add('tao-state-success');
        resultBox.className = 'tao-signup-result tao-result-success';
        resultBox.innerHTML =
          '<p class="tao-signup-success-headline">You\u2019re in.</p>' +
          '<p>The next issue of <em>The Tao of Clinical Touch</em> will come to you directly.</p>';
        resultBox.style.display = 'block';
        pushEvent('tao_email_signup_success', { signup_code: data.code || 'unknown' });
      } else {
        // Error state — show message, re-enable form.
        resultBox.className = 'tao-signup-result tao-result-error';
        resultBox.textContent = data.message || 'Something went wrong. Please try again.';
        resultBox.style.display = 'block';
        button.disabled = false;
        button.textContent = 'Receive New Issues';
        pushEvent('tao_email_signup_error', { error_code: data.code || 'unknown' });
      }
    };

    xhr.onerror = function () {
      resultBox.className = 'tao-signup-result tao-result-error';
      resultBox.textContent = 'Something went wrong. Please try again.';
      resultBox.style.display = 'block';
      button.disabled = false;
      button.textContent = 'Receive New Issues';
      pushEvent('tao_email_signup_error', { error_code: 'network' });
    };

    xhr.send(JSON.stringify({ email: email, source: CONFIG.source }));
  });
})();
