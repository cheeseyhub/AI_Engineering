import logging
import time
from torch.utils.tensorboard import SummaryWriter # type: ignore

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("training.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)



try:
    import torch
    import torch.nn as nn
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False





class Timer:
    def __init__(self,name=""):
        self.name = name;

    def __enter__(self):
        self.start = time.perf_counter();

    def __exit__(self,*args):
        elapsed = time.perf_counter() - self.start;
        print(f"[{self.name} { elapsed:.4f}]s")



def check_shapes(model, sample_input):
    print(f"Input: {sample_input.shape}")
    hooks = []

    def make_hook(name):
        def hook(module, inp, out):
            in_shape = inp[0].shape if isinstance(inp, tuple) else inp.shape
            out_shape = out.shape if hasattr(out, "shape") else type(out)
            print(f"  {name}: {in_shape} -> {out_shape}")
        return hook

    for name, module in model.named_modules():
        hooks.append(module.register_forward_hook(make_hook(name)))

    with torch.no_grad():
        model(sample_input)

    for h in hooks:
        h.remove()


def demo_timing():
    print("\n--- 2. Timing Code Sections ---")

    with Timer("matrix multiply 1000x1000"):
        a = torch.randn(1000, 1000)
        b = torch.randn(1000, 1000)
        _ = a @ b

    with Timer("matrix multiply 5000x5000"):
        a = torch.randn(5000, 5000)
        b = torch.randn(5000, 5000)
        _ = a @ b


def debug_print(name ,tensor):
    print(f" {name} : shape= {tensor.shape}, dtype={tensor.dtype}",
          f"device={tensor.device}",
          f"min={tensor.min().item():.4f}, max={tensor.max().item():.4f}",
          f"mean={tensor.mean().item():.4f}",
          f"has_nan={tensor.isnan().any().items()}"

    )




def training_step(model,batch,criterion,optimizer):
    inputs, labels = batch;
    outputs = model(inputs);
    loss = criterion(outputs,labels);
    if loss.item() > 100 or torch.isnan(loss):
        breakpoint();
    loss.backward()
    optimizer.step();




def detect_nan(model, loss, step):
    if torch.isnan(loss):
        print(f"NaN loss at step {step}")
        for name, param in model.named_parameters():
            if param.grad is not None:
                if torch.isnan(param.grad).any():
                    print(f"  NaN gradient in {name}")
                if torch.isinf(param.grad).any():
                    print(f"  Inf gradient in {name}")
        return True
    return False

def check_data_leakage(train_set, test_set, id_column="id"):
    train_ids = set(train_set[id_column].tolist())
    test_ids = set(test_set[id_column].tolist())
    overlap = train_ids & test_ids
    if overlap:
        print(f"DATA LEAKAGE: {len(overlap)} samples in both train and test")
        return True
    return False


def check_devices(model, *tensors):
    model_device = next(model.parameters()).device
    print(f"Model device: {model_device}")
    for i, t in enumerate(tensors):
        if t.device != model_device:
            print(f"  WARNING: tensor {i} on {t.device}, model on {model_device}")

