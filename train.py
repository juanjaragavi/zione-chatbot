import replicate

training = replicate.trainings.create(
    version="meta/llama-2-7b:527827021d8756c7ab79fde0abbfaac885c37a3ed5fe23c7465093f0878d55ef",
    input={
        "train_data": "https://huggingface.co/datasets/JuanJaramillo/samsum-sp/blob/main/samsumsp.jsonl",
        "num_train_epochs": 1
    },
    destination="juanjaragavi/web-scraper"
)

print(training)
