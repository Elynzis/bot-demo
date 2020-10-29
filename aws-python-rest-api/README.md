Demo simple REST API with Python running on AWS Lambda and API Gateway using the traditional Serverless Framework.

## Prerequisites
1. Install [Node.js](https://nodejs.org/en/)
2. Create [AWS Account](https://aws.amazon.com/free/) (Free tier)
3. Create [AWS IAM User and Access Key](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)
4. Install Serverless
```
npm install serverless -g
```

## Setup
1. Clone the repository
```
git clone https://github.com/Elynzis/bot-demo.git
cd bot-demo/aws-python-rest-api
```

## Usage

**Set Credentials**
```
serverless config credentials --provider aws --key <YOUR_AWS_ACCESS_KEY> --secret <YOUR_AWS_SECRET_ACCESS_KEY> --profile my-demo-profile
```

**Deploy**
```
serverless deploy --aws-profile my-demo-profile
```

**Invoke the function locally**

```
serverless invoke local --function hello
```

**Invoke the function**

```
curl --location --request GET '<YOUR_ENDPOINT>' \
--header 'x-api-key: <YOUR_API_KEY>'
```
