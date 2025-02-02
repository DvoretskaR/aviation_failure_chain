# Optimierte Umgebung
$env:OMP_NUM_THREADS = [Environment]::ProcessorCount
$env:HF_HUB_ENABLE_HF_TRANSFER = "1"

# Virtuelle Umgebung
if (-not (Test-Path .venv)) {
    python -m venv .venv
}
.\.venv\Scripts\activate

pip install -r requirements.txt

# Start
python main.py