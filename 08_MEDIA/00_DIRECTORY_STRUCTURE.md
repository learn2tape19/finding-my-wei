# Media Operating System — Directory Structure
## Finding My Wei v1.0

**Document Classification:** Repository Organization  
**Authority:** Publishing Director  
**Effective Date:** June 26, 2026  
**Status:** Reference Guide  
**Review Cycle:** Annual

---

## OVERVIEW

This document describes the recommended directory structure for the Media Operating System repository.

**Principles:**
- Content organized by campaign, not by date
- Linked to Project Atlas and Finding My Wei
- Searchable and maintainable
- Growth-accommodating
- Analytics embedded

---

## ROOT DIRECTORY STRUCTURE

```
08_MEDIA/
├── 00_GOVERNANCE/                    [Foundational documents]
├── 01_CAMPAIGNS/                     [Active and archived campaigns]
├── 02_ASSETS/                        [Reusable content & templates]
├── 03_ARCHIVES/                      [Completed campaigns]
├── 04_ANALYTICS/                     [Performance data & reporting]
├── 05_PLATFORMS/                     [Platform-specific guidelines]
├── 06_BRAND/                         [Brand guidelines & standards]
├── 07_WORKFLOWS/                     [Process documentation]
├── README.md                         [Repository overview]
└── INDEX.md                          [Search & navigation]
```

---

## DIRECTORY 00: GOVERNANCE

**Purpose:** Foundational documents governing all publishing decisions

```
00_GOVERNANCE/
├── EDITORIAL_CONSTITUTION.md         [Highest governing document]
├── EDITORIAL_STANDARDS_MANUAL.md     [Operational standards]
├── CAMPAIGN_TAXONOMY.md              [Campaign classification system]
├── EDITORIAL_REVIEW_CHECKLIST.md     [Publishing gate/quality standards]
├── EDITORIAL_DECISION_TREE.md        [Decision-making framework]
├── PUBLISHING_GOVERNANCE_DIAGRAM.md  [Organizational structure]
└── AMENDMENT_LOG.md                  [History of changes to documents]
```

**File naming:** Governance documents use CAPS_AND_UNDERSCORES

---

## DIRECTORY 01: CAMPAIGNS

**Purpose:** Active, in-progress, and recent campaigns organized by project and type

```
01_CAMPAIGNS/

├── ATLAS_01_THERAPEUTIC_ALLIANCE/
│   ├── CAMPAIGN_01_FRAMEWORK_RESEARCH/
│   │   ├── campaign_plan.md                    [Campaign overview & strategy]
│   │   ├── ASSETS/
│   │   │   ├── anchor_paper.md                [Primary research document]
│   │   │   ├── LinkedIn_article_v1.md         [LinkedIn-optimized version]
│   │   │   ├── website_article_v1.md          [Website article]
│   │   │   ├── email_course_series.md         [5-email sequence]
│   │   │   ├── instagram_carousel.md          [Carousel script & captions]
│   │   │   ├── quotes_and_snippets.md         [15+ social media quotes]
│   │   │   ├── newsletter_feature.md          [Newsletter curated section]
│   │   │   ├── discussion_guide.md            [For educators/group learning]
│   │   │   └── VIDEO/
│   │   │       ├── video_script.md
│   │   │       ├── video_specs.txt
│   │   │       └── editing_notes.md
│   │   │
│   │   ├── REVIEWS/
│   │   │   ├── research_review.md             [Phase 1: Sources & evidence]
│   │   │   ├── fact_review.md                 [Phase 2: Accuracy verification]
│   │   │   ├── message_review.md              [Phase 3: Clarity & alignment]
│   │   │   ├── visual_review.md               [Phase 4: Design & formatting]
│   │   │   ├── platform_review.md             [Phase 5: Platform adaptation]
│   │   │   ├── ethics_review.md               [Phase 6: Integrity & conflicts]
│   │   │   └── final_approval.md              [Phase 7: Editor-in-Chief sign-off]
│   │   │
│   │   ├── SCHEDULE/
│   │   │   ├── publication_schedule.txt       [Dates & platforms]
│   │   │   ├── content_calendar.csv           [Buffer/scheduling tool export]
│   │   │   └── email_send_times.txt           [Optimal send timing]
│   │   │
│   │   └── ANALYTICS/
│   │       ├── week_1_performance.md          [First 7 days metrics]
│   │       ├── week_2_performance.md
│   │       ├── week_3_performance.md
│   │       ├── week_4_performance.md
│   │       ├── monthly_summary.md             [Aggregate performance]
│   │       ├── audience_feedback.md           [Comments & responses]
│   │       ├── learning_documented.md         [Key insights & lessons]
│   │       └── performance_vs_targets.md      [Target vs. actual]
│   │
│   └── CAMPAIGN_02_[NEXT_CAMPAIGN_NAME]/
│       └── [Same structure as CAMPAIGN_01]
│
├── ATLAS_02_SIDEKICK_AIR/
│   ├── CAMPAIGN_01_PRODUCT_CONCEPT/
│   │   └── [Same structure as above]
│   │
│   └── CAMPAIGN_02_LAUNCH_COORDINATED/
│       └── [Same structure as above]
│
└── STANDALONE_CAMPAIGNS/                    [Non-Atlas campaigns]
    ├── RESEARCH_TRANSLATION_NERVOUS_SYSTEM/
    │   └── [Campaign structure]
    │
    ├── CASE_REFLECTION_CLINICAL_DISCOVERY/
    │   └── [Campaign structure]
    │
    └── PROFESSIONAL_DEVELOPMENT_PORTABLE_PRACTICE/
        └── [Campaign structure]
```

**File naming conventions:**
- campaign_plan.md (lowercase, underscores)
- research_review.md (phase names with underscore)
- week_1_performance.md (week # with underscore)
- linkedin_article_v1.md (platform + version)

---

## DIRECTORY 02: ASSETS

**Purpose:** Reusable content, templates, and templates

```
02_ASSETS/

├── TEMPLATES/
│   ├── campaign_plan_template.md          [Blank campaign plan]
│   ├── research_review_template.md        [Blank research review]
│   ├── linkedin_article_template.md       [LinkedIn structure guide]
│   ├── instagram_carousel_template.md     [5-7 slide structure]
│   ├── email_course_template.md           [5-email sequence structure]
│   ├── newsletter_section_template.md     [Newsletter format]
│   ├── website_article_template.md        [Website structure + SEO]
│   └── review_checklist_template.txt      [Editorial review checklist]
│
├── FRAMEWORKS/
│   ├── therapeutic_alliance_framework.md  [Atlas 01 framework]
│   ├── nervous_system_safety_framework.md [Key framework]
│   ├── clinical_reasoning_model.md        [Teaching framework]
│   └── [Additional frameworks as created]
│
├── GRAPHICS_LIBRARY/
│   ├── LOGOS/
│   │   ├── finding_my_wei_logo.png
│   │   ├── finding_my_wei_wordmark.png
│   │   └── [Alternative formats]
│   │
│   ├── ICONS/
│   │   ├── check_icon.svg
│   │   ├── arrow_icon.svg
│   │   ├── nervous_system_icon.svg
│   │   └── [As needed]
│   │
│   ├── BRAND_COLORS/
│   │   └── color_palette.txt               [Hex codes & usage]
│   │
│   └── VISUAL_ELEMENTS/
│       ├── texture_backgrounds/
│       ├── divider_graphics/
│       └── decorative_elements/
│
├── COPY_LIBRARY/
│   ├── email_subject_lines.txt            [High-performing subject lines]
│   ├── linkedin_hooks.txt                 [Opening lines that work]
│   ├── call_to_action_options.txt         [CTAs for different contexts]
│   ├── testimonial_quotes.txt             [Proven quotes]
│   └── disclaimer_templates.txt           [Standard disclaimers]
│
├── SOCIAL_MEDIA/
│   ├── instagram_carousel_specs.txt       [Technical specifications]
│   ├── linkedin_optimal_timing.txt        [Best days/times]
│   ├── email_open_rate_benchmarks.txt     [Performance targets]
│   ├── hashtag_strategy.txt               [Platform-specific hashtags]
│   └── content_calendar_template.csv      [Blank calendar]
│
├── RESEARCH_RESOURCES/
│   ├── citation_formats.txt               [APA, Chicago, etc.]
│   ├── credible_sources_list.md           [Vetted resources]
│   ├── research_databases.txt             [Where to find studies]
│   └── fact_checking_resources.md         [Verification tools]
│
└── REFERENCE_DOCS/
    ├── audience_personas.md               [Who are we writing for?]
    ├── brand_voice_guide.md               [Tone & style guide]
    ├── platform_best_practices.md         [LinkedIn, Instagram, etc.]
    └── competitor_analysis.md             [Market positioning]
```

---

## DIRECTORY 03: ARCHIVES

**Purpose:** Completed campaigns moved out of active work

```
03_ARCHIVES/

├── 2026/
│   ├── Q1/
│   │   ├── CAMPAIGN_NAME_001_archive/
│   │   │   ├── final_performance_summary.md
│   │   │   ├── learning_documented.md
│   │   │   ├── all_assets.zip               [Complete campaign files]
│   │   │   └── index.md                     [What's in this archive]
│   │   │
│   │   └── CAMPAIGN_NAME_002_archive/
│   │       └── [Same structure]
│   │
│   ├── Q2/
│   │   └── [Campaigns completed in Q2]
│   │
│   ├── Q3/
│   │   └── [Campaigns completed in Q3]
│   │
│   └── Q4/
│       └── [Campaigns completed in Q4]
│
└── 2027/
    ├── Q1/
    │   └── [Next year's archives]
    └── [Continues...]
```

**Archival process:**
1. Campaign marked as "complete" with final analytics
2. All files moved to 03_ARCHIVES with year/quarter organization
3. Final performance summary generated
4. Learning documented for future reference
5. All assets zipped for backup
6. Index created for easy reference

---

## DIRECTORY 04: ANALYTICS

**Purpose:** Centralized performance data and reporting

```
04_ANALYTICS/

├── MONTHLY_REPORTS/
│   ├── 2026_january_report.md              [All platform metrics]
│   ├── 2026_february_report.md
│   ├── 2026_march_report.md
│   └── [Monthly through current]
│
├── QUARTERLY_REPORTS/
│   ├── 2026_Q1_report.md                   [Aggregate Q1 data]
│   ├── 2026_Q2_report.md
│   └── [Quarterly reports]
│
├── ANNUAL_REPORTS/
│   ├── 2026_annual_report.md               [Full year summary]
│   └── [Future years]
│
├── PLATFORM_ANALYTICS/
│   ├── linkedin_metrics.csv                [Ongoing LinkedIn data]
│   ├── instagram_metrics.csv               [Ongoing Instagram data]
│   ├── website_traffic.csv                 [Website analytics]
│   ├── email_performance.csv               [Email metrics]
│   ├── youtube_metrics.csv                 [Video performance]
│   └── social_aggregated.csv               [All platforms combined]
│
├── AUDIENCE_DATA/
│   ├── audience_growth_trend.csv           [Subscribers/followers over time]
│   ├── audience_demographics.md            [Who's following?]
│   ├── engagement_patterns.md              [When/what gets engagement]
│   ├── top_content_performers.md           [Best performing pieces]
│   └── audience_feedback_themes.md         [Common questions/requests]
│
├── CONVERSION_DATA/
│   ├── course_enrollment_metrics.csv       [Course sign-ups]
│   ├── product_sales_metrics.csv           [Product purchases]
│   ├── email_signup_sources.csv            [Where subscribers come from]
│   ├── landing_page_performance.csv        [Page conversion rates]
│   └── funnel_analysis.md                  [Full funnel performance]
│
├── CONTENT_PERFORMANCE/
│   ├── content_by_type.md                  [Which types perform best?]
│   ├── content_by_platform.md              [Platform performance comparison]
│   ├── content_by_topic.md                 [Which topics engage most?]
│   ├── word_count_analysis.md              [Length vs. performance]
│   └── publish_time_analysis.md            [When is best to publish?]
│
└── REPORTING_TEMPLATES/
    ├── monthly_report_template.md
    ├── quarterly_report_template.md
    ├── annual_report_template.md
    └── performance_dashboard_template.csv
```

**Analytics workflow:**
- Weekly: Publishing Director updates platform metrics
- Monthly: Editorial Director generates monthly report
- Quarterly: Comprehensive quarterly analysis
- Annual: Full-year review with Editor-in-Chief

---

## DIRECTORY 05: PLATFORMS

**Purpose:** Platform-specific guidelines and standards

```
05_PLATFORMS/

├── LINKEDIN/
│   ├── linkedin_strategy.md                [Overall approach]
│   ├── linkedin_best_practices.md          [What works on LinkedIn]
│   ├── linkedin_content_guidelines.md      [Format & timing]
│   ├── linkedin_engagement_strategy.md     [Growing followers]
│   └── linkedin_case_studies.md            [Examples of success]
│
├── INSTAGRAM/
│   ├── instagram_strategy.md               [Overall approach]
│   ├── instagram_best_practices.md         [What works on Instagram]
│   ├── instagram_visual_guidelines.md      [Design standards]
│   ├── instagram_carousel_specs.md         [Technical requirements]
│   ├── instagram_hashtag_strategy.md       [Hashtag selection]
│   ├── instagram_stories_guidelines.md     [Story formatting]
│   └── instagram_case_studies.md           [Examples]
│
├── WEBSITE/
│   ├── website_strategy.md                 [Overall approach]
│   ├── website_content_guidelines.md       [Writing for web]
│   ├── website_seo_guidelines.md           [SEO best practices]
│   ├── website_design_standards.md         [Visual & layout]
│   ├── website_user_experience.md          [Navigation & usability]
│   ├── website_technical_specs.md          [CMS, hosting, etc.]
│   └── website_case_studies.md             [What pages work best?]
│
├── EMAIL/
│   ├── email_strategy.md                   [Overall approach]
│   ├── email_design_guidelines.md          [Template & visual]
│   ├── email_copywriting.md                [Writing for email]
│   ├── email_segmentation.md               [List management]
│   ├── email_deliverability.md             [Inbox optimization]
│   ├── email_automation.md                 [Sequences & triggers]
│   └── email_case_studies.md               [Performance examples]
│
├── VIDEO/
│   ├── video_strategy.md                   [Overall approach]
│   ├── video_production_guidelines.md      [Creating videos]
│   ├── video_technical_specs.md            [Dimensions, bitrate, etc.]
│   ├── video_editing_process.md            [From raw to final]
│   ├── video_distribution.md               [Where to publish]
│   └── video_performance_metrics.md        [How to measure success]
│
├── PODCAST/
│   ├── podcast_strategy.md                 [Overall approach]
│   ├── podcast_production.md               [Recording & editing]
│   ├── podcast_distribution.md             [Platforms & feeds]
│   ├── podcast_promotion.md                [Getting listeners]
│   └── podcast_case_studies.md             [Performance data]
│
└── OTHER_PLATFORMS/
    ├── twitter_strategy.md
    ├── tiktok_strategy.md
    ├── youtube_strategy.md
    └── [Additional platforms as adopted]
```

---

## DIRECTORY 06: BRAND

**Purpose:** Brand identity and consistency standards

```
06_BRAND/

├── BRAND_GUIDELINES.md                     [Master brand guide]
├── BRAND_VOICE.md                          [Tone & personality]
├── VISUAL_IDENTITY/
│   ├── logo_specifications.pdf
│   ├── color_palette.txt
│   ├── typography_guide.md
│   ├── imagery_style.md
│   └── design_system.md
│
├── LANGUAGE_STYLE/
│   ├── tone_examples.md                    [How we sound]
│   ├── word_choices.md                     [Preferred terminology]
│   ├── common_phrases.txt                  [Signature phrases]
│   └── style_guide.txt                     [Grammar & punctuation]
│
├── BRAND_STORY/
│   ├── brand_origin.md                     [Why Finding My Wei exists]
│   ├── mission_statement.md                [What we're about]
│   ├── values_statement.md                 [Core values]
│   └── brand_promise.md                    [What we deliver]
│
├── COMPETITIVE_POSITIONING/
│   ├── market_positioning.md               [Where we fit]
│   ├── unique_value_proposition.md         [Why choose us?]
│   ├── competitor_comparison.md            [How we compare]
│   └── differentiation_strategy.md         [What makes us different]
│
└── APPROVAL_PROCESS/
    ├── brand_usage_guidelines.md           [When/how to use brand elements]
    ├── logo_usage_rules.md                 [Logo placement & sizing]
    ├── brand_violation_checklist.md        [What not to do]
    └── approval_process.md                 [Who approves brand decisions]
```

---

## DIRECTORY 07: WORKFLOWS

**Purpose:** Process documentation and team training

```
07_WORKFLOWS/

├── CAMPAIGN_WORKFLOWS/
│   ├── campaign_planning_workflow.md       [How to plan a campaign]
│   ├── content_creation_workflow.md        [How to create content]
│   ├── editorial_review_workflow.md        [7-phase review process]
│   ├── scheduling_workflow.md              [How to schedule content]
│   ├── analytics_review_workflow.md        [How to measure performance]
│   └── archival_workflow.md                [How to archive campaign]
│
├── ROLE_SPECIFIC/
│   ├── editor_in_chief_responsibilities.md    [Drew's role]
│   ├── editorial_director_responsibilities.md (ChatGPT role)
│   ├── content_director_responsibilities.md   (Claude role)
│   ├── creative_director_responsibilities.md  (Firefly role)
│   └── publishing_director_responsibilities.md (Buffer role)
│
├── TOOLS_TRAINING/
│   ├── buffer_usage_guide.md               [How to use Buffer]
│   ├── google_analytics_guide.md           [How to track metrics]
│   ├── github_workflow.md                  [How to use GitHub]
│   ├── adobe_express_guide.md              [Design tool]
│   └── [Additional tool training]
│
├── DECISION_PROCESSES/
│   ├── how_to_use_decision_tree.md         [Using decision trees]
│   ├── escalation_process.md               [When/how to escalate]
│   ├── dispute_resolution.md               [How to resolve conflicts]
│   └── amendment_process.md                [How to change Constitution]
│
└── TRAINING_MATERIALS/
    ├── new_team_member_orientation.md      [Onboarding guide]
    ├── editorial_standards_training.md     [Standards overview]
    ├── campaign_taxonomy_training.md       [Campaign types]
    └── values_training.md                  [Constitutional values]
```

---

## FILE NAMING CONVENTIONS

**General principles:**
- Use lowercase
- Use underscores for spaces
- Use version numbers for revisions
- Use dates for time-sensitive documents
- Use descriptive names that indicate content

**Examples:**

```
campaign_plan.md               [Good]
Campaign Plan.md               [Bad - capital letters]
CP.md                          [Bad - unclear abbreviation]

linkedin_article_v1.md         [Good - includes platform & version]
linkedin_article_final.md      [Bad - "final" versions change]
article.md                     [Bad - unclear which platform]

research_review_phase_1.md     [Good - includes phase]
research_review.md             [Bad - missing phase info]

week_1_performance.md          [Good - includes week number]
1_performance.md               [Bad - doesn't indicate week]
performance_week_1.md          [OK but less standard]
```

---

## LINKING & CROSS-REFERENCING

**Link campaigns to Project Atlas:**
```
campaign_plan.md includes at top:
├─ Project: Atlas 01 - Therapeutic Alliance
├─ Derived from: PROJECT_ATLAS_01_DECISION.md
├─ Related campaigns: [link to other campaigns]
└─ Finding My Wei connection: [how it enriches FMW]
```

**Link campaigns to Finding My Wei:**
```
Each campaign includes:
├─ Knowledge graph nodes impacted
├─ Learning that goes back to FMW
├─ Analytics that inform future research
└─ Intellectual estate contribution
```

---

## SEARCH & NAVIGATION

**Index files for easy finding:**

```
README.md                      [Repository overview]
INDEX.md                       [Searchable index of all files]
RECENT_CAMPAIGNS.md            [Currently active campaigns]
ARCHIVES_INDEX.md              [Complete archives listing]
TOPIC_INDEX.md                 [Organized by topic]
PLATFORM_INDEX.md              [Organized by platform]
AUTHOR_INDEX.md                [Which director created what]
```

---

## BACKUP & ARCHIVAL STRATEGY

**Backup schedule:**
- Weekly: All files backed up to secure cloud storage
- Monthly: Analytics data exported and archived
- Quarterly: Complete campaign archives created
- Annual: Full-year archives created

**Retention:**
- Active campaigns: In 01_CAMPAIGNS/
- Completed campaigns: Moved to 03_ARCHIVES/
- Analytics: Retained permanently in 04_ANALYTICS/
- Templates: Kept current in 02_ASSETS/

---

## GROWTH PLANNING

**As volume increases:**

- Campaigns grow to 30+: Consider sub-organizing by year
- Assets exceed 100: Consider sub-organizing by asset type
- Analytics accumulate: Archive old metrics, keep recent accessible
- Team grows: Add team-specific directories in WORKFLOWS/

**Scaling structure:**
```
01_CAMPAIGNS/
├── 2026/
│   ├── ATLAS_01/
│   │   └── [Campaigns]
│   └── ATLAS_02/
│       └── [Campaigns]
│
└── 2027/
    ├── ATLAS_01/
    └── ATLAS_02/
```

---

## IMPLEMENTATION CHECKLIST

When setting up the Media Operating System repository:

- [ ] Create directory structure above
- [ ] Copy governance documents into 00_GOVERNANCE/
- [ ] Create templates in 02_ASSETS/TEMPLATES/
- [ ] Set up GitHub repository with this structure
- [ ] Create README.md with overview
- [ ] Create INDEX.md for navigation
- [ ] Set up analytics tracking
- [ ] Establish backup schedule
- [ ] Train team on structure & naming
- [ ] Document any local variations
- [ ] Create search/retrieval guide
- [ ] Plan quarterly reviews

---

**Document Version:** 1.0  
**Approved by:** Drew Freedman, Editor-in-Chief  
**Effective Date:** June 26, 2026  
**Next Review:** June 2027  

**For questions on directory structure:** Contact Publishing Director  
**For questions on governance:** Contact Editor-in-Chief  
**For questions on file naming:** See conventions section above