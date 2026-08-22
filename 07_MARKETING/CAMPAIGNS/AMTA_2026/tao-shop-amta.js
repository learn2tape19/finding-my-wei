/**
 * THE TAO OF CLINICAL TOUCH — AMTA 2026 CAMPAIGN SHOP
 * Forked from production tao-shop.js (read-only baseline).
 *
 * Changes from production:
 * - shopSource: "amta_2026" campaign attribution
 * - shopPath: "/shop-amta/"
 * - Fulfillment selector: amta_pickup (FREE, default) or shipping ($5)
 * - AMTA campaign context banner in hero
 * - Price/total/shipping display updates on fulfillment change
 * - Checkout URLs switch based on fulfillment selection
 * - Analytics: shop_source + fulfillment_method on all events
 * - New event: tao_fulfillment_select
 *
 * Usage:
 * 1) Create a WordPress page at /shop-amta/
 * 2) Add an Elementor HTML widget (or raw HTML block).
 * 3) Add: <div id="tao-shop-root" data-tao-shop-campaign="amta_2026"></div>
 * 4) Paste this script below the div.
 *
 * IMPORTANT:
 * Replace AMTA_PICKUP checkout URLs before launch.
 */

(() => {
  "use strict";

  /* ----------------------------------------------------------------
   * CAMPAIGN GUARD — only initialize on the AMTA page.
   * Production /shop/ must never execute this script.
   * ---------------------------------------------------------------- */
  const root = document.getElementById("tao-shop-root");
  if (!root) return;
  if (root.getAttribute("data-tao-shop-campaign") !== "amta_2026") return;

  const CONFIG = {
    /* Fulfillment-specific Stripe Payment Links.
     * Shipping variants reuse the proven production links.
     * Pickup variants need NEW Stripe links at pickup pricing (no $5 shipping).
     * Placeholder URLs trigger the guardrail alert until replaced. */
    checkout: {
      signed: {
        amta_pickup:  "https://buy.stripe.com/3cI00j5j9btv8egakGfUQ03",
        shipping:     "https://buy.stripe.com/aFa3cvaDtapr0LO9gCfUQ00"
      },
      personalized: {
        amta_pickup:  "https://buy.stripe.com/3cI7sLcLBcxzgKMdwSfUQ02",
        shipping:     "https://buy.stripe.com/bJeeVd26X413dyA1OafUQ01"
      }
    },
    amazonUrl: "https://www.amazon.com/dp/B0GVTZZS99",
    bulkContactUrl: "/bulk-orders/",
    shopPath: "/shop-amta/",
    shopSource: "amta_2026",
    bookCoverUrl: "https://taoclinicaltouch.com/wp-content/uploads/2026/04/Tao_Clinical_Touch_Cover_front_shadow-2.png",
    authorImageUrl: "https://taoclinicaltouch.com/wp-content/uploads/2026/04/Drew_Headshot_Tao-1.png",
    amtaArtworkUrl: "https://taoclinicaltouch.com/wp-content/uploads/2026/08/AMTA_2026_DENVER.png",
    currency: "USD",
    analyticsTransport: "dataLayer",

    fulfillment: {
      default: "amta_pickup",
      options: {
        amta_pickup: { label: "Pick up at AMTA National", fee: 0, detail: "Denver, August 27–29 — FREE" },
        shipping:    { label: "Ship to me", fee: 5, detail: "Standard U.S. Shipping — $5.00" }
      }
    }
  };

  /* ----------------------------------------------------------------
   * PRODUCTS
   * ---------------------------------------------------------------- */
  const PRODUCTS = {
    signed: { price: 19.99, name: "Signed Copy" },
    personalized: { price: 24.99, name: "Personalized + Signed" }
  };

  /* ----------------------------------------------------------------
   * STATE
   * ---------------------------------------------------------------- */
  let currentFulfillment = CONFIG.fulfillment.default;

  function getFee() {
    return CONFIG.fulfillment.options[currentFulfillment].fee;
  }

  function getTotal(productKey) {
    return PRODUCTS[productKey].price + getFee();
  }

  function getCheckoutUrl(productKey) {
    return CONFIG.checkout[productKey][currentFulfillment];
  }

  /* ----------------------------------------------------------------
   * CSS — identical to production + fulfillment selector styles
   * ---------------------------------------------------------------- */
  const css = `
    :root{
      --tao-navy:#182633;
      --tao-navy-2:#0d0f3f;
      --tao-gold:#B8860B;
      --tao-ivory:#F7F3EA;
      --tao-ink:#17202a;
      --tao-muted:#6c7480;
      --tao-white:#ffffff;
      --tao-rule:rgba(24,38,51,.16);
      --tao-shadow:0 22px 60px rgba(13,15,63,.12);
      --tao-radius:22px;
      --tao-serif: "Cormorant Garamond", Georgia, "Times New Roman", serif;
      --tao-sans: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    #tao-shop-root,
    #tao-shop-root *{box-sizing:border-box}

    #tao-shop-root{
      background:var(--tao-ivory);
      color:var(--tao-ink);
      font-family:var(--tao-sans);
      font-size:1rem;
      line-height:1.55;
      overflow:hidden;
    }

    .tao-shell{max-width:1180px;margin:0 auto;padding:0 28px}
    .tao-section{padding:92px 0}
    .tao-kicker{
      color:var(--tao-gold);
      font-size:.78rem;
      font-weight:800;
      letter-spacing:.15em;
      text-transform:uppercase;
      margin:0 0 18px;
    }
    .tao-title,
    .tao-h2,
    .tao-h3{
      font-family:var(--tao-serif);
      color:var(--tao-navy);
      font-weight:500;
      letter-spacing:-.02em;
      margin:0;
    }
    .tao-title{font-size:clamp(2.32rem,4.24vw,4rem);line-height:1;max-width:980px}
    .tao-subtitle{
      margin:22px 0 0;
      max-width:760px;
      font-size:clamp(1rem,1.35vw,1.2rem);
      color:#34414d;
    }
    .tao-h2{font-size:clamp(1.52rem,2.8vw,2.64rem);line-height:1.06}
    .tao-h3{font-size:1.45rem;line-height:1.15}

    .tao-hero{
      position:relative;
      background:
        radial-gradient(circle at 80% 18%, rgba(184,134,11,.14), transparent 32%),
        linear-gradient(180deg, #fbf8f1 0%, var(--tao-ivory) 100%);
      padding:110px 0 76px;
      border-bottom:1px solid var(--tao-rule);
    }
    .tao-hero-grid{
      display:grid;
      grid-template-columns:1.25fr .75fr;
      gap:64px;
      align-items:center;
    }
    .tao-hero-copy blockquote{
      border-left:3px solid var(--tao-gold);
      margin:36px 0 0;
      padding:0 0 0 22px;
      color:var(--tao-navy);
      font-family:var(--tao-serif);
      font-size:clamp(1.3rem,1.95vw,1.8rem);
      line-height:1.3;
    }
    .tao-book-stage{
      display:flex;
      justify-content:center;
      align-items:center;
      min-height:520px;
      position:relative;
    }
    .tao-book-stage:before{
      content:"";
      position:absolute;
      width:82%;
      aspect-ratio:1;
      background:rgba(184,134,11,.12);
      border-radius:50%;
      filter:blur(2px);
    }
    .tao-book{
      position:relative;
      width:min(320px,82%);
      filter:drop-shadow(0 28px 34px rgba(13,15,63,.23));
      transform:rotate(2deg);
      z-index:1;
    }
    .tao-book img{display:block;width:100%;height:auto;border-radius:4px}
    .tao-image-placeholder{
      width:100%;aspect-ratio:2/3;background:linear-gradient(145deg,var(--tao-navy-2),#223856);
      display:grid;place-items:center;color:var(--tao-white);padding:30px;text-align:center;
      font-family:var(--tao-serif);font-size:1.4rem;border-radius:4px;
    }

    .tao-offers{
      background:var(--tao-white);
      border-top:1px solid var(--tao-rule);
      border-bottom:1px solid var(--tao-rule);
    }
    .tao-section-head{max-width:780px;margin-bottom:44px}
    .tao-grid-2{display:grid;grid-template-columns:1fr 1fr;gap:28px}
    .tao-card{
      background:#fff;
      border:1px solid var(--tao-rule);
      border-radius:var(--tao-radius);
      padding:36px;
      box-shadow:var(--tao-shadow);
      position:relative;
    }
    .tao-card.featured{
      border:2px solid var(--tao-gold);
      transform:translateY(-8px);
    }
    .tao-badge{
      display:inline-block;
      background:var(--tao-gold);
      color:#fff;
      border-radius:999px;
      padding:7px 12px;
      font-size:.72rem;
      letter-spacing:.09em;
      text-transform:uppercase;
      font-weight:800;
      margin-bottom:18px;
    }
    .tao-price{font-family:var(--tao-serif);font-size:2.08rem;color:var(--tao-navy);margin:18px 0 4px;line-height:1}
    .tao-shipping{color:var(--tao-muted);font-size:.95rem;margin-bottom:22px}
    .tao-card p{color:#3f4a55}
    .tao-btn{
      display:inline-flex;
      align-items:center;
      justify-content:center;
      gap:10px;
      min-height:54px;
      border-radius:999px;
      padding:0 24px;
      font-family:var(--tao-sans);
      font-size:1rem;
      line-height:1.2;
      white-space:nowrap;
      font-weight:800;
      text-decoration:none!important;
      border:1px solid transparent;
      transition:.2s ease;
      cursor:pointer;
      width:100%;
      margin-top:18px;
    }
    .tao-btn-primary{background:var(--tao-navy);color:#fff!important}
    .tao-btn-primary:hover{transform:translateY(-1px);background:var(--tao-navy-2)}
    .tao-btn-gold{background:var(--tao-gold);color:#fff!important}
    .tao-btn-gold:hover{transform:translateY(-1px);filter:brightness(.96)}
    .tao-btn-outline{border-color:var(--tao-navy);color:var(--tao-navy)!important;background:transparent}
    .tao-btn-outline:hover{background:var(--tao-navy);color:#fff!important}

    .tao-copy-band{background:var(--tao-navy);color:#e8edf2}
    .tao-copy-band .tao-h2,
    .tao-copy-band .tao-h3{color:#fff}
    .tao-copy-band p{color:#d8e0e7}
    .tao-copy-columns{
      display:grid;grid-template-columns:.85fr 1.15fr;gap:70px;align-items:start;
    }
    .tao-prompt{
      font-family:var(--tao-serif);
      font-size:clamp(1.6rem,2.08vw,1.95rem);
      color:#fff;
      margin:28px 0 0;
      line-height:1.28;
    }
    .tao-list{
      display:grid;grid-template-columns:1fr 1fr;gap:12px 28px;padding:0;margin:28px 0 0;list-style:none
    }
    .tao-list li{
      position:relative;padding-left:22px;color:#d8e0e7;
    }
    .tao-list li:before{
      content:"";position:absolute;left:0;top:.62em;width:8px;height:8px;border-radius:50%;background:var(--tao-gold)
    }

    .tao-author-grid{
      display:grid;grid-template-columns:.72fr 1.28fr;gap:58px;align-items:center
    }
    .tao-author-image{
      background:#e7e3da;border-radius:var(--tao-radius);overflow:hidden;min-height:420px;box-shadow:var(--tao-shadow)
    }
    .tao-author-image img{width:100%;height:100%;object-fit:cover;display:block}
    .tao-author-placeholder{display:grid;place-items:center;min-height:420px;color:var(--tao-muted);padding:30px;text-align:center}
    .tao-signoff{font-family:var(--tao-serif);font-size:1.45rem;color:var(--tao-navy);margin-top:26px}

    .tao-testimonials{background:#f0ece3}
    .tao-quote-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:36px}
    .tao-quote{
      background:#fff;border:1px solid var(--tao-rule);border-radius:var(--tao-radius);padding:30px;
      min-height:250px;display:flex;flex-direction:column;justify-content:flex-start
    }
    .tao-quote p{font-family:var(--tao-serif);font-size:1.25rem;color:var(--tao-navy);margin:0}
    .tao-quote p + p{margin-top:1.25em}
    .tao-quote cite{font-style:normal;font-weight:800;color:#4b5660;margin-top:24px}
    .tao-quote cite span{display:block;font-weight:600;font-size:.86rem;color:var(--tao-muted);margin-top:5px}
    .tao-quote.placeholder{border-style:dashed}

    .tao-bulk{
      background:linear-gradient(120deg,#fff 0%,#fbf6e9 100%);
    }
    .tao-bulk-card{
      border:1px solid rgba(184,134,11,.32);
      border-radius:var(--tao-radius);
      padding:48px;
      display:grid;grid-template-columns:1.2fr .8fr;gap:34px;align-items:center;
      background:#fff;
    }

    .tao-amazon{
      border-top:1px solid var(--tao-rule);
      border-bottom:1px solid var(--tao-rule);
      text-align:center;
      background:#fff;
    }
    .tao-amazon .tao-section-head{margin:0 auto 24px}
    .tao-inline-actions{display:flex;justify-content:center;gap:14px;flex-wrap:wrap}
    .tao-inline-actions .tao-btn{width:auto;min-width:220px}

    .tao-faq details{
      border-top:1px solid var(--tao-rule);
      padding:0;
    }
    .tao-faq details:last-child{border-bottom:1px solid var(--tao-rule)}
    .tao-faq summary{
      cursor:pointer;font-weight:800;color:var(--tao-navy);font-size:1.05rem;
      padding:22px 0;
    }
    .tao-faq details[open] summary{padding-bottom:13px}
    .tao-faq details p{max-width:760px;color:#48545f;margin:0;padding-bottom:22px}

    .tao-final{
      background:var(--tao-navy-2);
      color:#fff;
      text-align:center;
      position:relative;
    }
    .tao-final .tao-h2{color:#fff}
    .tao-final p{max-width:760px;margin:20px auto;color:#d9def0;font-size:1.1rem}
    .tao-final .tao-inline-actions{margin-top:30px}

    .tao-ripple{
      width:100%;
      height:18px;
      opacity:.72;
      margin-top:70px;
      position:relative;
      overflow:hidden;
    }
    .tao-ripple:before,
    .tao-ripple:after{
      content:"";
      position:absolute;
      left:50%;
      transform:translateX(-50%);
      border:1px solid var(--tao-gold);
      border-radius:50%;
      width:560px;height:80px;top:2px;
    }
    .tao-ripple:after{width:760px;height:110px;top:5px;opacity:.55}

    .tao-note{
      font-size:.86rem;color:var(--tao-muted);margin-top:14px
    }

    /* ------------------------------------------------------------------
       SEMANTIC TYPE TIERS  @1440
       ------------------------------------------------------------------ */
    .tao-copy-columns > div:last-child > p{font-size:1.19rem;line-height:1.66;color:#dbe0ef}
    .tao-copy-columns > div:last-child > p:first-of-type{font-size:1.44rem;line-height:1.52}
    .tao-list li{font-size:1.06rem;line-height:1.5}
    .tao-author-grid > div:last-child > p:not(.tao-kicker){font-size:1.19rem;line-height:1.7}
    .tao-author-grid > div:last-child > h2 + p:not(.tao-kicker){font-size:1.44rem;line-height:1.55}
    .tao-bulk-card p:not(.tao-kicker){font-size:1.25rem;line-height:1.62;max-width:56ch}
    .tao-amazon .tao-section-head p:not(.tao-kicker){font-size:1.06rem;line-height:1.6}
    .tao-card p{font-size:1rem;line-height:1.6}
    .tao-faq details p{font-size:1rem;line-height:1.62}
    .tao-testimonials .tao-h2{font-size:clamp(1.55rem,2vw,1.88rem);line-height:1.16}
    .tao-author-grid > div:last-child > p:not(.tao-kicker){font-size:1.35rem;line-height:1.62;max-width:58ch}
    .tao-author-grid > div:last-child > h2 + p:not(.tao-kicker){font-size:1.44rem;line-height:1.56;max-width:56ch}
    .tao-signoff{font-size:1.25rem;line-height:1.5}

    @media (max-width:900px){
      .tao-hero-grid,
      .tao-copy-columns,
      .tao-author-grid,
      .tao-bulk-card{grid-template-columns:1fr}
      .tao-grid-2,
      .tao-quote-grid{grid-template-columns:1fr}
      .tao-list{grid-template-columns:1fr}
      .tao-book-stage{min-height:380px}
      .tao-card.featured{transform:none}
      .tao-section{padding:68px 0}
      .tao-hero{padding-top:76px}
    }

    @media (max-width:560px){
      .tao-shell{padding:0 20px}
      .tao-card,.tao-bulk-card{padding:26px}
      .tao-title{font-size:2.32rem}
      .tao-inline-actions{flex-direction:column}
      .tao-inline-actions .tao-btn{width:100%}
    }

    /* ==================================================================
       TYPE LOCK — absolute px, scoped to #tao-shop-root
       ================================================================== */
    #tao-shop-root .tao-kicker{font-size:12.5px}
    #tao-shop-root .tao-title{font-size:clamp(37.12px,4.24vw,64px)}
    #tao-shop-root .tao-subtitle{font-size:clamp(16px,1.35vw,19.2px)}
    #tao-shop-root .tao-h2{font-size:clamp(24.32px,2.8vw,42.24px)}
    #tao-shop-root .tao-testimonials .tao-h2{font-size:clamp(24.8px,2vw,30.08px)}
    #tao-shop-root .tao-h3{font-size:23.2px}
    #tao-shop-root .tao-hero-copy blockquote{font-size:clamp(20.8px,1.95vw,28.8px)}
    #tao-shop-root .tao-prompt{font-size:clamp(25.6px,2.08vw,31.2px)}
    #tao-shop-root .tao-price{font-size:33.28px}
    #tao-shop-root .tao-shipping{font-size:15.2px}
    #tao-shop-root .tao-badge{font-size:11.5px}
    #tao-shop-root .tao-signoff{font-size:20px;line-height:1.5}
    #tao-shop-root .tao-note{font-size:13.8px}
    #tao-shop-root a.tao-btn{font-family:var(--tao-sans);font-size:16px;line-height:1.2;white-space:nowrap}
    #tao-shop-root .tao-quote p{font-size:20px;line-height:1.55}
    #tao-shop-root .tao-quote cite{font-size:16px;line-height:1.35}
    #tao-shop-root .tao-quote cite span{font-size:13.8px;line-height:1.4}
    #tao-shop-root .tao-copy-columns > div:last-child > p{font-size:19px;line-height:1.66}
    #tao-shop-root .tao-copy-columns > div:last-child > p:first-of-type{font-size:23px;line-height:1.52}
    #tao-shop-root .tao-list li{font-size:17px;line-height:1.5}
    #tao-shop-root .tao-author-grid > div:last-child > p:not(.tao-kicker){font-size:21.6px;line-height:1.62;max-width:58ch}
    #tao-shop-root .tao-author-grid > div:last-child > h2 + p:not(.tao-kicker){font-size:23px;line-height:1.56;max-width:56ch}
    #tao-shop-root .tao-card p{font-size:16px;line-height:1.6}
    #tao-shop-root .tao-bulk-card p:not(.tao-kicker){font-size:20px;line-height:1.62;max-width:56ch}
    #tao-shop-root .tao-amazon .tao-section-head p:not(.tao-kicker){font-size:17px;line-height:1.6}
    #tao-shop-root .tao-faq summary{font-size:16.8px}
    #tao-shop-root .tao-faq details p{font-size:16px;line-height:1.62}
    #tao-shop-root .tao-final p{font-size:17.6px}

    @media (max-width:560px){
      #tao-shop-root .tao-title{font-size:37.12px}
    }

    /* ==================================================================
       AMTA FULFILLMENT SELECTOR — new UI for this campaign only
       ================================================================== */
    #tao-shop-root .tao-amta-banner{
      background:var(--tao-navy);
      color:#fff;
      text-align:center;
      padding:14px 28px;
      font-size:15px;
      font-weight:600;
      letter-spacing:.02em;
    }
    #tao-shop-root .tao-amta-banner strong{
      color:var(--tao-gold);
    }

    #tao-shop-root .tao-amta-decal{
      position:absolute;
      top:28px;
      right:32px;
      width:clamp(100px, 10vw, 140px);
      height:auto;
      transform:rotate(-5deg);
      border-radius:10px;
      box-shadow:0 4px 14px rgba(0,0,0,.13);
      z-index:10;
      pointer-events:none;
    }
    #tao-shop-root .tao-amta-decal img{
      display:block;
      width:100%;
      height:auto;
      border-radius:10px;
    }
    @media (max-width:900px){
      #tao-shop-root .tao-amta-decal{
        width:90px;
        top:18px;
        right:18px;
      }
    }
    @media (max-width:560px){
      #tao-shop-root .tao-amta-decal{
        width:72px;
        top:12px;
        right:12px;
      }
    }

    #tao-shop-root .tao-fulfillment{
      margin-bottom:36px;
      padding:28px 32px;
      background:var(--tao-ivory);
      border:1px solid var(--tao-rule);
      border-radius:var(--tao-radius);
    }
    #tao-shop-root .tao-fulfillment-options{
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:12px;
      margin-top:14px;
    }
    #tao-shop-root .tao-fulfillment-option{
      display:flex;
      flex-direction:column;
      padding:16px 20px;
      border:2px solid var(--tao-rule);
      border-radius:14px;
      cursor:pointer;
      transition:border-color .15s, background .15s;
      position:relative;
    }
    #tao-shop-root .tao-fulfillment-option:hover{
      border-color:var(--tao-navy);
    }
    #tao-shop-root .tao-fulfillment-option.selected{
      border-color:var(--tao-gold);
      background:rgba(184,134,11,.06);
    }
    #tao-shop-root .tao-fulfillment-option input[type="radio"]{
      position:absolute;
      opacity:0;
      width:0;
      height:0;
    }
    #tao-shop-root .tao-fulfillment-label{
      font-weight:800;
      color:var(--tao-navy);
      font-size:15px;
    }
    #tao-shop-root .tao-fulfillment-detail{
      font-size:13px;
      color:var(--tao-muted);
      margin-top:4px;
    }

    @media (max-width:560px){
      #tao-shop-root .tao-fulfillment-options{grid-template-columns:1fr}
    }
  `;

  /* ----------------------------------------------------------------
   * IMAGES
   * ---------------------------------------------------------------- */
  const cover = CONFIG.bookCoverUrl && CONFIG.bookCoverUrl !== "BOOK_COVER_IMAGE_URL"
    ? `<img decoding="async" src="${CONFIG.bookCoverUrl}" alt="The Tao of Clinical Touch book cover">`
    : `<div class="tao-image-placeholder">The Tao of Clinical Touch<br><small>The Neuroscience of Permission</small></div>`;

  const authorImage = CONFIG.authorImageUrl && CONFIG.authorImageUrl !== "AUTHOR_IMAGE_URL"
    ? `<img decoding="async" src="${CONFIG.authorImageUrl}" alt="Drew Freedman">`
    : `<div class="tao-author-placeholder">Add approved Drew Freedman author image here.</div>`;

  /* ----------------------------------------------------------------
   * HTML — production layout + AMTA campaign context + fulfillment
   * ---------------------------------------------------------------- */
  const html = `
    <style>${css}</style>

    <div class="tao-amta-banner">
      <strong>Going to AMTA National?</strong> Order now and pick up your signed copy from Drew in Denver — no shipping charge.
    </div>

    <main class="tao-shop">
      <section class="tao-hero">
        <div class="tao-amta-decal" aria-hidden="true"><img decoding="async" src="${CONFIG.amtaArtworkUrl}" alt="AMTA 2026 National Convention — Denver, August 27–29"></div>
        <div class="tao-shell tao-hero-grid">
          <div class="tao-hero-copy">
            <p class="tao-kicker">Signed Edition Shop</p>
            <h1 class="tao-title">The Tao of Clinical Touch</h1>
            <p class="tao-subtitle"><strong>The Neuroscience of Permission.</strong><br>
            A signed copy, sent directly from the author.</p>
            <blockquote>Technique matters. But technique works differently when the nervous system is ready to receive it.</blockquote>
          </div>
          <div class="tao-book-stage">
            <div class="tao-book">${cover}</div>
          </div>
        </div>
        <div class="tao-ripple" aria-hidden="true"></div>
      </section>

      <section class="tao-section tao-offers" id="choose-your-copy">
        <div class="tao-shell">
          <div class="tao-section-head">
            <p class="tao-kicker">Choose your copy</p>
            <h2 class="tao-h2">Two ways to receive the Tao.</h2>
          </div>

          <div class="tao-fulfillment" role="radiogroup" aria-label="Fulfillment method">
            <p class="tao-kicker" style="margin-bottom:0">How would you like to receive your book?</p>
            <div class="tao-fulfillment-options">
              <label class="tao-fulfillment-option selected" data-fulfillment="amta_pickup">
                <input type="radio" name="fulfillment" value="amta_pickup" checked>
                <span class="tao-fulfillment-label">Pick up at AMTA National — FREE</span>
                <span class="tao-fulfillment-detail">AMTA National Pickup — Denver, August 27–29</span>
              </label>
              <label class="tao-fulfillment-option" data-fulfillment="shipping">
                <input type="radio" name="fulfillment" value="shipping">
                <span class="tao-fulfillment-label">Ship to me — $5.00</span>
                <span class="tao-fulfillment-detail">Standard U.S. Shipping</span>
              </label>
            </div>
          </div>

          <div class="tao-grid-2">
            <article class="tao-card">
              <h3 class="tao-h3">Signed Copy</h3>
              <div class="tao-price" data-product="signed">$19.99</div>
              <div class="tao-shipping" data-shipping="signed">FREE — AMTA National Pickup</div>
              <p>A new paperback copy of <em>The Tao of Clinical Touch</em>, personally signed by Drew Freedman.</p>
              <a class="tao-btn tao-btn-primary" data-checkout="signed" href="${getCheckoutUrl('signed')}">Order a Signed Copy</a>
            </article>

            <article class="tao-card featured">
              <span class="tao-badge">Recommended</span>
              <h3 class="tao-h3">Personalized + Signed</h3>
              <div class="tao-price" data-product="personalized">$24.99</div>
              <div class="tao-shipping" data-shipping="personalized">FREE — AMTA National Pickup</div>
              <p>Tell me who the book is for and I\u2019ll personally inscribe and sign it before sending it to you.</p>
              <a class="tao-btn tao-btn-gold" data-checkout="personalized" href="${getCheckoutUrl('personalized')}">Personalize My Copy</a>
              <div class="tao-note">Includes a brief personal inscription. Specific wording requests are considered but not guaranteed.</div>
            </article>
          </div>
        </div>
      </section>

      <section class="tao-section tao-copy-band">
        <div class="tao-shell tao-copy-columns">
          <div>
            <p class="tao-kicker">This isn\u2019t another book of techniques.</p>
            <h2 class="tao-h2">You already have techniques.</h2>
            <p class="tao-prompt">The deeper question is: what does this nervous system need in order to permit change?</p>
          </div>
          <div>
            <p><em>The Tao of Clinical Touch</em> explores the conditions that allow technique to become more effective: presence, precision, alliance, regulation, restraint, communication, and permission.</p>
            <p>It asks clinicians to consider not simply <strong>what should I do?</strong> but <strong>what should govern what I do?</strong></p>
            <ul class="tao-list">
              <li>Why the clinical encounter begins before touch</li>
              <li>How the practitioner becomes part of the treatment environment</li>
              <li>Why protective guarding can change what assessment reveals</li>
              <li>How pressure can become dialogue rather than imposition</li>
              <li>How language, expectation, and predictability influence care</li>
              <li>Why lasting change ultimately belongs to the person receiving treatment</li>
            </ul>
          </div>
        </div>
      </section>

      <section class="tao-section">
        <div class="tao-shell tao-author-grid">
          <div class="tao-author-image">${authorImage}</div>
          <div>
            <p class="tao-kicker">From my hands to yours</p>
            <h2 class="tao-h2">A copy directly from the author.</h2>
            <p>I wrote <em>The Tao of Clinical Touch</em> after more than two decades of trying to understand why some clinical encounters create meaningful change while others don\u2019t.</p>
            <p>What began years ago as a way of communicating the standards of my own clinical practice eventually became something larger\u2014a framework for examining how we enter the room, how we listen, how we touch, and how we recognize when a body is ready for change.</p>
            <p>These signed copies give me an opportunity to complete that circle personally.</p>
            <p>Whether you\u2019re adding the Tao to your own clinical library, giving it to a colleague, or sharing it with a therapist whose work has mattered to you, I\u2019m grateful that it has found its way into your hands.</p>
            <div class="tao-signoff">Walk the Way.<br>\u2014 Drew Freedman</div>
            <a class="tao-btn tao-btn-gold" style="max-width:330px" data-checkout="personalized" href="${getCheckoutUrl('personalized')}">Get a Personalized Copy</a>
          </div>
        </div>
      </section>

      <section class="tao-section tao-testimonials">
        <div class="tao-shell">
          <div class="tao-section-head">
            <p class="tao-kicker">What respected clinicians are saying</p>
            <h2 class="tao-h2">Read. Reflect. Reconsider the room.</h2>
          </div>
          <div class="tao-quote-grid">
            <article class="tao-quote">
              <p>The Tao of Clinical Touch offers a thoughtful and inspiring re-imagining of the power of gentle, invitational, listening bodywork. Driven by the principles of presence, precision, and respect, Drew Freedman\u2019s vision emphasizes how the therapeutic alliance must set the tone for all aspects of a client-practitioner interaction.</p>
              <cite>\u2014 Ruth Werner<span>Author, A Massage Therapist\u2019s Guide to Pathology</span></cite>
            </article>
            <article class="tao-quote">
              <p>There is so much wisdom in these pages. The profession has needed such a book, and massage therapists, both new and those with years of experience, will find it invaluable. Too often, the focus has been on what is done, not the approach and the underlying processes that help to create the environment where change is possible.</p>
              <cite>\u2014 Doug Nelson, BCMT<span>Founder, Precision Neuromuscular Therapy</span><span>Past President, Massage Therapy Foundation</span></cite>
            </article>
            <article class="tao-quote">
              <p>What I appreciate most about this approach is that it doesn\u2019t replace clinical precision; it creates the environment where that precision can actually work. Drew calls it \u2018physiological permission,\u2019 and to me, that is the ultimate clinical metric. Without it, we\u2019re just moving tissue; with it, we\u2019re facilitating healing.</p>
              <cite>\u2014 Whitney Lowe<span>Founder, Academy of Clinical Massage</span></cite>
            </article>
          </div>
        </div>
      </section>

      <section class="tao-section tao-bulk">
        <div class="tao-shell">
          <div class="tao-bulk-card">
            <div>
              <p class="tao-kicker">Clinics \u2022 Schools \u2022 CE \u2022 Events</p>
              <h2 class="tao-h2">Buying for more than one person?</h2>
              <p>Need books for a class, clinic, school, organization, or professional group? Contact us about multiple-copy orders.</p>
            </div>
            <div>
              <a class="tao-btn tao-btn-outline" data-cta="bulk" href="${CONFIG.bulkContactUrl}">Request Multiple Copies</a>
            </div>
          </div>
        </div>
      </section>

      <section class="tao-section tao-amazon">
        <div class="tao-shell">
          <div class="tao-section-head">
            <p class="tao-kicker">Prefer Amazon?</p>
            <h2 class="tao-h2">Just want the book?</h2>
            <p>The standard paperback edition remains available through Amazon for $14.99. The direct shop is for readers who want a signed or personalized copy from Drew.</p>
          </div>
          <div class="tao-inline-actions">
            <a class="tao-btn tao-btn-outline" data-cta="amazon" href="${CONFIG.amazonUrl}" target="_blank" rel="noopener">Buy on Amazon \u2014 $14.99</a>
            <a class="tao-btn tao-btn-primary" data-checkout="personalized" href="${getCheckoutUrl('personalized')}">Make It Personal \u2014 $24.99</a>
          </div>
        </div>
      </section>

      <section class="tao-section tao-faq">
        <div class="tao-shell">
          <div class="tao-section-head">
            <p class="tao-kicker">Questions</p>
            <h2 class="tao-h2">Before you order.</h2>
          </div>

          <details>
            <summary>What\u2019s the difference between Signed and Personalized + Signed?</summary>
            <p>A Signed Copy includes Drew\u2019s signature. A Personalized + Signed Copy includes a brief inscription made out specifically to you or the person receiving the book, plus Drew\u2019s signature.</p>
          </details>

          <details>
            <summary>Can I send a personalized copy as a gift?</summary>
            <p>Yes. Enter the recipient\u2019s name and any short context requested during checkout.</p>
          </details>

          <details>
            <summary>How does AMTA National pickup work?</summary>
            <p>Select \u201cPick up at AMTA National\u201d during checkout. After your order is confirmed, we\u2019ll coordinate your pickup location at the convention in Denver, August 27\u201329. No shipping charge applies.</p>
          </details>

          <details>
            <summary>How long will my order take to ship?</summary>
            <p>If you choose shipping, signed orders typically leave our hands within 3\u20135 business days. This is our handling time, not a carrier delivery estimate.</p>
          </details>

          <details>
            <summary>Where do you ship?</summary>
            <p>Shipping fulfillment is limited to U.S. addresses. AMTA National pickup is available regardless of location.</p>
          </details>

          <details>
            <summary>Can I order copies for my clinic, class, or organization?</summary>
            <p>Yes. Use the bulk-order inquiry and include the approximate number of copies you need.</p>
          </details>
        </div>
      </section>

      <section class="tao-section tao-final">
        <div class="tao-shell">
          <p class="tao-kicker">The Tao of Clinical Touch</p>
          <h2 class="tao-h2">Technique gives us something to do.<br>Clinical maturity teaches us when, why, and how much.</h2>
          <p>Choose the copy that fits the way you want to receive the Tao.</p>
          <div class="tao-inline-actions">
            <a class="tao-btn tao-btn-outline" style="border-color:#fff;color:#fff!important" data-checkout="signed" href="${getCheckoutUrl('signed')}">Signed \u2014 $19.99</a>
            <a class="tao-btn tao-btn-gold" data-checkout="personalized" href="${getCheckoutUrl('personalized')}">Personalized + Signed \u2014 $24.99</a>
          </div>
          <div class="tao-ripple" aria-hidden="true"></div>
        </div>
      </section>
    </main>
  `;

  root.innerHTML = html;

  /* ----------------------------------------------------------------
   * FULFILLMENT STATE MANAGEMENT
   * ---------------------------------------------------------------- */
  function updateFulfillmentUI() {
    const fee = getFee();
    const isPickup = currentFulfillment === "amta_pickup";

    // Update shipping labels on product cards
    root.querySelectorAll("[data-shipping]").forEach(el => {
      el.textContent = isPickup
        ? "FREE \u2014 AMTA National Pickup"
        : "+ $5.00 Standard U.S. Shipping";
    });

    // Update checkout URLs on all CTAs
    root.querySelectorAll("a[data-checkout]").forEach(link => {
      const key = link.getAttribute("data-checkout");
      link.setAttribute("href", getCheckoutUrl(key));
    });

    // Update final section CTA labels with totals
    const finalActions = root.querySelector(".tao-final .tao-inline-actions");
    if (finalActions) {
      const signedBtn = finalActions.querySelector('[data-checkout="signed"]');
      const persBtn = finalActions.querySelector('[data-checkout="personalized"]');
      if (signedBtn) signedBtn.textContent = `Signed \u2014 $${getTotal("signed").toFixed(2)}`;
      if (persBtn) persBtn.textContent = `Personalized + Signed \u2014 $${getTotal("personalized").toFixed(2)}`;
    }

    // Update fulfillment option visual state
    root.querySelectorAll(".tao-fulfillment-option").forEach(opt => {
      const val = opt.getAttribute("data-fulfillment");
      opt.classList.toggle("selected", val === currentFulfillment);
      opt.querySelector("input").checked = (val === currentFulfillment);
    });
  }

  // Fulfillment selector event listeners
  root.querySelectorAll(".tao-fulfillment-option").forEach(opt => {
    opt.addEventListener("click", () => {
      const newMethod = opt.getAttribute("data-fulfillment");
      if (newMethod === currentFulfillment) return;
      currentFulfillment = newMethod;
      updateFulfillmentUI();

      // Analytics: tao_fulfillment_select
      emit("tao_fulfillment_select", {
        fulfillment_method: currentFulfillment,
        product_type: "all"
      });
    });

    // Keyboard: Enter/Space on the label
    opt.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        opt.click();
      }
    });
  });

  /* ----------------------------------------------------------------
   * ANALYTICS — extended with shop_source + fulfillment_method
   * ---------------------------------------------------------------- */
  const ANALYTICS = {
    listId: "tao_signed_shop",
    listName: "Tao Signed Edition Shop",
    items: {
      signed: {
        item_id: "tao_signed_19_99",
        item_name: "The Tao of Clinical Touch \u2014 Signed Copy",
        price: 19.99,
        shipping: 5.00
      },
      personalized: {
        item_id: "tao_personalized_24_99",
        item_name: "The Tao of Clinical Touch \u2014 Personalized + Signed",
        price: 24.99,
        shipping: 5.00
      }
    }
  };

  const ATTRIBUTION_KEY = "tao_shop_attribution";
  const UTM_KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"];

  function captureAttribution() {
    let stored = {};
    try {
      stored = JSON.parse(sessionStorage.getItem(ATTRIBUTION_KEY) || "{}");
    } catch (e) {
      stored = {};
    }

    const params = new URLSearchParams(window.location.search);
    const incoming = {};
    UTM_KEYS.forEach(key => {
      const value = params.get(key);
      if (value) incoming[key] = value;
    });

    const ref = params.get("ref");
    if (ref) incoming.referral_code = ref;

    const attribution = Object.keys(incoming).length ? incoming : stored;

    try {
      sessionStorage.setItem(ATTRIBUTION_KEY, JSON.stringify(attribution));
    } catch (e) { /* Private browsing */ }

    return attribution;
  }

  const attribution = captureAttribution();

  function emit(eventName, payload) {
    const data = Object.assign({
      event: eventName,
      shop_version: "v1",
      shop_source: CONFIG.shopSource,
      page_path: CONFIG.shopPath
    }, attribution, payload || {});

    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ items: undefined });
    window.dataLayer.push(data);
  }

  function placementOf(el) {
    const section = el.closest("section");
    if (!section) return "unknown";
    const named = Array.from(section.classList)
      .find(c => c.startsWith("tao-") && c !== "tao-section");
    return named ? named.replace("tao-", "") : "unknown";
  }

  // view_item_list — shop rendered
  emit("view_item_list", {
    item_list_id: ANALYTICS.listId,
    item_list_name: ANALYTICS.listName,
    fulfillment_method: currentFulfillment,
    items: [
      Object.assign({ index: 0 }, ANALYTICS.items.signed),
      Object.assign({ index: 1 }, ANALYTICS.items.personalized)
    ]
  });

  // select_item + begin_checkout — Stripe CTAs
  root.querySelectorAll("a[data-checkout]").forEach(link => {
    link.addEventListener("click", () => {
      const href = link.getAttribute("href") || "";
      if (href.includes("STRIPE_PAYMENT_LINK") || href.includes("AMTA_PICKUP")) return;

      const key = link.getAttribute("data-checkout");
      const item = ANALYTICS.items[key];
      if (!item) return;

      const placement = placementOf(link);
      const fee = getFee();
      const eventItem = Object.assign({ quantity: 1 }, item, { shipping: fee });

      emit("select_item", {
        item_list_id: ANALYTICS.listId,
        item_list_name: ANALYTICS.listName,
        cta_placement: placement,
        cta_label: link.textContent.trim(),
        fulfillment_method: currentFulfillment,
        items: [eventItem]
      });

      emit("begin_checkout", {
        currency: CONFIG.currency,
        value: item.price + fee,
        product_value: item.price,
        shipping: fee,
        checkout_type: key,
        cta_placement: placement,
        fulfillment_method: currentFulfillment,
        items: [eventItem]
      });
    });
  });

  // amazon_click
  root.querySelectorAll('a[data-cta="amazon"]').forEach(link => {
    link.addEventListener("click", () => {
      emit("amazon_click", {
        outbound_url: CONFIG.amazonUrl,
        cta_placement: placementOf(link),
        product_value: 14.99,
        currency: CONFIG.currency
      });
    });
  });

  // bulk_inquiry_click
  root.querySelectorAll('a[data-cta="bulk"]').forEach(link => {
    link.addEventListener("click", () => {
      emit("bulk_inquiry_click", {
        destination: CONFIG.bulkContactUrl,
        cta_placement: placementOf(link)
      });
    });
  });

  // faq_open
  const faqSeen = new Set();
  root.querySelectorAll(".tao-faq details").forEach((item, index) => {
    item.addEventListener("toggle", () => {
      if (!item.open) return;
      const summary = item.querySelector("summary");
      const question = summary ? summary.textContent.trim() : "question_" + index;
      if (faqSeen.has(question)) return;
      faqSeen.add(question);
      emit("faq_open", { faq_question: question, faq_index: index });
    });
  });

  // Guardrail: Prevent clicks on placeholder checkout URLs.
  root.querySelectorAll('a[data-checkout]').forEach(link => {
    link.addEventListener('click', (event) => {
      const href = link.getAttribute('href') || '';
      if (href.includes('STRIPE_PAYMENT_LINK') || href.includes('AMTA_PICKUP')) {
        event.preventDefault();
        alert('This checkout link has not been configured yet. Please select "Ship to me" or contact Drew directly.');
      }
    });
  });
})();
