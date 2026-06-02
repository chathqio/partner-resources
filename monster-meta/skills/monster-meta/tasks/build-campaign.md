<purpose>
Deploy a campaign plan to Meta via the MCP API. Creates the campaign, ad set, creative, and ad in sequence — all in PAUSED status. Runs the pre-launch checklist before offering to activate.
</purpose>

<user-story>
As a performance marketer, I want to deploy my approved campaign plan directly to Meta without leaving Claude Code, so that I can go from strategy to live campaign in a single workflow.
</user-story>

<when-to-use>
- After completing /monster-meta plan and approving the campaign plan
- When you have a campaign spec ready to deploy
- Entry point routes here via /monster-meta build
</when-to-use>

<context>
@context/account-config.md
@checklists/pre-launch.md
</context>

<references>
@frameworks/advertising/meta/facebook/chunks/01-campaign-architecture.md (for hierarchy validation)
@frameworks/advertising/meta/facebook/chunks/06-placements-automation.md (for placement config)
</references>

<steps>

<step name="locate_plan" priority="first">
Get the campaign plan to build from.

1. Check if a campaign plan was just produced by /monster-meta plan in this session
   - If yes: "I have the plan from your planning session. Use it?"
   - Wait for confirmation

2. If no recent plan, ask:
   - "Paste your campaign plan or provide the key details: objective, audience, budget, creative assets."

3. Parse and validate required fields:
   - Account ID (from account-config.md or ask)
   - Objective (must be ODAX format)
   - Budget (daily or lifetime, in cents)
   - Targeting spec (geo, age, interests/behaviors)
   - Creative assets (image path/URL, copy, headline, CTA)

4. Confirm: "Ready to build: {campaign_name} — {objective}, ${budget}/day, {audience_summary}. Proceed?"

**Wait for confirmation before creating anything.**
</step>

<step name="create_campaign">
Create the campaign shell.

1. Call `create_campaign` with:
   - account_id from account-config
   - name following naming convention
   - objective (ODAX)
   - status: PAUSED
   - bid_strategy
   - daily_budget or lifetime_budget (in cents)
   - special_ad_categories if applicable

2. Capture the returned campaign_id

3. Report: "Campaign created: {name} (ID: {campaign_id}) — PAUSED"
</step>

<step name="create_adset">
Create the ad set within the campaign.

1. If creative assets need uploading, call `upload_ad_image` first and capture image_hash

2. Call `create_adset` with:
   - account_id, campaign_id
   - name following naming convention
   - optimization_goal (mapped from objective)
   - billing_event: IMPRESSIONS (standard)
   - targeting spec (validated in plan step)
   - daily_budget or lifetime_budget (if using ABO instead of CBO)
   - bid_strategy, bid_amount/bid_constraints if applicable
   - start_time/end_time if scheduled
   - status: PAUSED

3. Capture the returned adset_id

4. Report: "Ad Set created: {name} (ID: {adset_id}) — PAUSED"
</step>

<step name="create_creative_and_ad">
Create the ad creative and link it to an ad.

1. If image not yet uploaded, call `upload_ad_image` and capture image_hash

2. Call `get_account_pages` to confirm page_id (or use account-config default)

3. Call `create_ad_creative` with:
   - account_id
   - name
   - page_id
   - image_hash (or video_id for video)
   - link_url (destination URL — **MUST include the required UTM params per `@context/account-config.md` UTM section**; `utm_content` must be the literal string `[[ad.name]]`, not a substituted value)
   - message (primary text)
   - headline (or headlines[] for multi-variant)
   - description (or descriptions[] for multi-variant)
   - call_to_action_type
   - instagram_actor_id (if applicable, from account-config)

4. Capture creative_id

5. Call `create_ad` with:
   - account_id
   - name
   - adset_id
   - creative_id
   - status: PAUSED

6. Capture ad_id

7. Report:
   ```
   Creative created: {name} (ID: {creative_id})
   Ad created: {name} (ID: {ad_id}) — PAUSED

   Campaign Structure:
   └── Campaign: {campaign_name} ({campaign_id}) — PAUSED
       └── Ad Set: {adset_name} ({adset_id}) — PAUSED
           └── Ad: {ad_name} ({ad_id}) — PAUSED
   ```
</step>

<step name="pre_launch_check">
Run the pre-launch checklist before offering activation.

1. Load @checklists/pre-launch.md
2. Verify each item against the created campaign:
   - Tracking: Pixel/CAPI configured?
   - Creative: Image specs correct? Copy within limits?
   - Targeting: Audience size viable? Geo correct?
   - Budget: Amount correct? Bid strategy matched?
   - Naming: Follows convention?
   - Status: Everything PAUSED?

3. Present checklist results

4. If all pass: "Pre-launch checklist passed. Want to activate this campaign? (This will set status to ACTIVE)"
5. If issues found: "Found {N} issues — fix before activating." List the issues.

**NEVER auto-activate. Always wait for explicit user confirmation.**
</step>

<step name="activate">
Activate the campaign if user confirms.

<if condition="user confirms activation">
1. Call `update_campaign` with status: ACTIVE
2. Call `update_adset` with status: ACTIVE
3. Call `update_ad` with status: ACTIVE
4. Report: "Campaign is now LIVE. Monitor with `/monster-meta audit`."
</if>

<if condition="user declines or wants changes">
Report: "Campaign stays PAUSED. Use the IDs above to make changes, or run `/monster-meta audit` to check performance after activation."
</if>
</step>

</steps>

<output>
Deployed campaign structure in Meta Ads:
- Campaign ID, Ad Set ID, Creative ID, Ad ID
- All entities created with confirmed settings
- Pre-launch checklist results
- Activation status (PAUSED or ACTIVE)
</output>

<acceptance-criteria>
- [ ] Campaign plan parsed with all required fields
- [ ] Campaign created in PAUSED status
- [ ] Ad set created with correct targeting and budget
- [ ] Creative created with correct assets and copy
- [ ] Ad created linking creative to ad set
- [ ] Pre-launch checklist executed
- [ ] No auto-activation — explicit user confirmation required
- [ ] Campaign structure summary displayed with all IDs
</acceptance-criteria>
