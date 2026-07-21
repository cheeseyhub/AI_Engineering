from datasets import load_dataset

# 01 Loading the glue (General language Understanding Evaluation );
# MRPC Microsoft Research Paraphrase Corpus

# dataset = load_dataset("nyu-mll/glue","mrpc",split="train");
# for row in dataset.take(5):
#     print(row)


# 02 C4 Dataset with streaming

# dataset = load_dataset('McAuley-Lab/Amazon-C4',split="test",streaming=True);


# for row in dataset.take(15):
#     print(row);




# 03 Converting database to Parquet and csv
# dataset = load_dataset("nyu-mll/glue","mrpc",split="train");
# dataset.to_csv("glue.csv");
# dataset.to_parquet("glue.parquet")


# 04 Creating a 70/15/15 train/val/test split with a fixed seed
dataset = load_dataset("nyu-mll/glue","mrpc",split="train");
split = dataset.train_test_split(test_size=0.3, seed=234);


train_val = split["train"].train_test_split(test_size=0.2143, seed=34);

train_ds = train_val["train"];
val_ds = train_val["test"];
test_ds = split["test"]
