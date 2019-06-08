# aws-whats-new

This is an AWS SAM App, refer to [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) for more info.

You should [create a parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-walk.html) on SSM called `chime.bot.url` with the URL for your [Amazon Chime] Bot.

For now it only integrates with Chime, the idea is actually sending a message to an SNS public topic so as people can subscribe and plug into their tool, like Slack, etc.

## Architecture Diagram

TODO a beautiful one.

## Lambda Functions

### StoreNewItems

Runs every minute, downloads the [rss feed](http://aws.amazon.com/new/feed/) and inserts each news in a DynamoDB table performing a [Conditional Write](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.ConditionalUpdate), inserting in the table only items that doesn't existt. That item insertion triggers another function, the `SendMessage`, listed below.

### SendMessage

Simply gets the DynamoDB item that had been recently inserted and posts to [Amazon Chime], reading the Chime Bot URL from a parameter from [AWS Parameter Store](https://aws.amazon.com/blogs/mt/tag/parameter-store/).

## Areas of Improvement

I'm downloading the full RSS every time, that's ugly, it would be good to have something that stores in the DynamoDB table a value containing the `last-modified:` HTTP response header for control, and HEADs the page first to check if the content had been changed, that would save me performance regarding HTTP get requests to the feed and money because DynamoDB consumes the WCU even though the Conditional Write is not satisfied.

:wq

[Amazon Chime]: (https://aws.amazon.com/chime/)