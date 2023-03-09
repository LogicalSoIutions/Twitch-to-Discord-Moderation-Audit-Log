# Twitch-to-Discord-Moderation-Audit-Log
Since Twitch doesn't have the greatest moderation audit log, I wanted a way to archive the mod actions easier so I built this. 

To get your auth token -> https://twitchtokengenerator.com/ -> Custom Scope Token -> channel:moderate OR moderation:read - I use channel:moderate as I use this token to get moderation access on the API level for LVNDMARK and a few other streamers

[Go here](https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/) to convert Twitch usernames to ID's for your `redemption_topic`

Example: `redemption_topic = "chat_moderator_actions.74992193.427632467"` - This is because 74992193 = my User ID and 427632467 = LVNDMARK's channel

To get your `webhook_url` you will need to go to the "settings" of the channel you want this to post the audit logs to and go to `Integrations` and then `Webhooks`

Click `New Webhook` - Name it - then `Copy Webhook URL`
