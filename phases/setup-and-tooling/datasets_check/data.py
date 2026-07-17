from datasets import load_dataset

# dataset =  load_dataset("stanfordnlp/imdb")
# print(dataset);
# print(dataset["train"][0])

# Streaming example for large dataset
# dataset = load_dataset("wikimedia/wikipedia", "20231101.en",split="train",streaming=True)
# for row in dataset.take(5):
#     print(row)



# Converting to csv json and parquet
# dataset = load_dataset("imdb", split="train")
# dataset.to_csv("imdb_train.csv")
# dataset.to_json("imdb_train.json")
# dataset.to_parquet("imdb_train.parquet")



dataset =  load_dataset("stanfordnlp/imdb",split="train")
split = dataset.train_test_split(test_size=0.2 , seed=42);
train_val = split["tain"].train_test_split(test_size=0.125, seed=42)


train_ds = train_val["train"];
val_ds = train_val["test"];
test_ds = split["test"];


print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}")
