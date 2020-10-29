Demo simple REST API with Python running on AWS Lambda and API Gateway using the traditional Serverless Framework.

## Prerequisites
1. Install Node.JS ..
2. Create AWS Account (Free tier)
3. Create AWS IAM User and get credentials
4. Install Serverless
```bash
npm install serverless -g
```

## Setup
1. Clone the repository
2. Serverless init TBD


## Usage

**Set Credentials**
```
$ serverless config credentials --provider aws --key <YOUR_AWS_ACCESS_KEY> --secret <YOUR_AWS_SECRET_ACCESS_KEY> --profile my-demo-profile
```

**Deploy**
```
$ serverless deploy --aws-profile my-demo-profile
```

**Invoke the function locally.**

```
serverless invoke local --function hello
```

**Invoke the function**

```
curl --location --request GET '<YOUR_ENDPOINT>' \
--header 'x-api-key: <YOUR_API_KEY>'
```


