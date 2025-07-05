# Lambda S3 Trigger Example

This Lambda function is triggered when a new file is uploaded to a specific S3 bucket.

## 🧠 How It Works

- Triggered by an S3 `putObject` event
- Logs the name of the file and the bucket
- Use it to test your first Lambda + S3 integration

## 📦 Files
- `handler.py` — the main Lambda function
- `event_sample.json` — example input event from S3

## 🛠️ How to Deploy (Quick Guide)
1. Create a Lambda function in AWS Console
2. Upload `handler.py` as zip or paste code
3. Set trigger: S3 bucket → All object create events

## 🧪 Sample Test Event
Check `event_sample.json` to simulate the S3 trigger.
