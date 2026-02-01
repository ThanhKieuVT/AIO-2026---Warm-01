# ======================================================
# 1️⃣ IMPORT LIBRARIES & CONFIGURATION
# ======================================================
import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf
from pathlib import Path

# Model Configuration
MODEL_FILENAME = "final_model.keras"  # Model file
DEFAULT_IMAGE_SIZE = 128              # Training image size
CONFIDENCE_THRESHOLD = 0.7            # Threshold to decide if it's a valid prediction

# ======================================================
# 2️⃣ LOAD MODEL (Runs once at startup)
# ======================================================
model_path = Path(MODEL_FILENAME)
if not model_path.exists():
    raise FileNotFoundError(f"❌ Model file not found: {MODEL_FILENAME}")

print("⏳ Loading model...")
model = tf.keras.models.load_model(str(model_path))
print("✅ Model loaded successfully!")

# ======================================================
# 3️⃣ CORE LOGIC (Inference)
# ======================================================
def predict_image(image, image_size):
    """
    Receives image from Gradio -> Processes it -> Returns prediction
    """
    # Safety check 1: No image uploaded
    if image is None:
        return None

    # Safety check 2: Fix 'NoneType' error if Gradio doesn't send size immediately
    if image_size is None:
        image_size = DEFAULT_IMAGE_SIZE

    # 1. Preprocess
    # Ensure image is in PIL format
    if not isinstance(image, Image.Image):
        pil_img = Image.fromarray(image)
    else:
        pil_img = image
        
    # Resize and normalize
    target_size = int(image_size)
    img = pil_img.convert("RGB").resize((target_size, target_size))
    x = np.array(img).astype(np.float32) / 255.0
    x = np.expand_dims(x, axis=0)  # Shape: (1, H, W, 3)

    # 2. Inference
    y = model.predict(x, verbose=0)

    # 3. Post-process & "Unknown" Handling
    p_cat, p_dog = 0.0, 0.0
    
    # ===== Case 1: Sigmoid (1 output neuron) =====
    if y.shape[-1] == 1:
        p_dog = float(y[0][0])
        p_cat = 1.0 - p_dog
    
    # ===== Case 2: Softmax (2 output neurons) =====
    elif y.shape[-1] == 2:
        p_cat = float(y[0][0])
        p_dog = float(y[0][1])
    
    else:
        return {"Error": 0.0}

    # 4. Check for "Not Dog or Cat" (Low Confidence)
    max_conf = max(p_cat, p_dog)
    
    # If confidence is too low, we classify as Unknown
    if max_conf < CONFIDENCE_THRESHOLD:
        return {
            "Unknown / Not a Pet ❓": 1.0 - max_conf, 
            "CAT 🐱": p_cat,
            "DOG 🐶": p_dog
        }

    return {"CAT 🐱": p_cat, "DOG 🐶": p_dog}

# ======================================================
# 4️⃣ GRADIO UI (Using Blocks for custom button names)
# ====================================================== 

with gr.Blocks(theme="default") as demo:
    gr.Markdown("# 🐶🐱 Cats vs Dogs Classifier")
    gr.Markdown("Upload an image of a dog or a cat. If the image is unclear, it will be labeled as Unknown.")
    
    with gr.Row():
        with gr.Column():
            input_img = gr.Image(type="pil", label="Upload Image")
            input_size = gr.Number(value=DEFAULT_IMAGE_SIZE, label="Image Size (Resize to)", minimum=32, maximum=512)
            # Đây là nơi mình đặt tên nút tùy ý
            classify_btn = gr.Button("Classify", variant="primary")
            reset_btn = gr.Button("Reset")
        
        with gr.Column():
            output_label = gr.Label(num_top_classes=3, label="Prediction Result")

    # Thiết lập sự kiện khi bấm nút
    classify_btn.click(
        fn=predict_image, 
        inputs=[input_img, input_size], 
        outputs=output_label
    )
    
    # Thiết lập nút Reset
    reset_btn.click(
        fn=lambda: [None, DEFAULT_IMAGE_SIZE, None], 
        inputs=[], 
        outputs=[input_img, input_size, output_label]
    )

# Launch App
if __name__ == "__main__":
    demo.launch()