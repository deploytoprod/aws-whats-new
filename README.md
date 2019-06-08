# aws-whats-new

This is an AWS SAM App, refer to [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) for more info.

You should create a parameter on SSM called `chime.bot.url` with the URL for your Chime Bot.

For now it only integrates with Chime, the idea is actually sending a message to an SNS public topic so as people can subscribe and plug into their tool, like Slack, etc.

