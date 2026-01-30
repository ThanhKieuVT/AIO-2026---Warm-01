# ======================================================
# 1️⃣ IMPORT THƯ VIỆN & CẤU HÌNH CHUNG
#    (KHÔNG LIÊN QUAN UI HAY MODEL TRỰC TIẾP)
# ======================================================

import streamlit as st          # Thư viện UI
import numpy as np              # Xử lý số
from PIL import Image           # Xử lý ảnh
import tensorflow as tf         # Load & chạy model
from pathlib import Path        # Xử lý đường dẫn file

# Cấu hình giao diện tổng thể của app (UI)
st.set_page_config(
    page_title="Cats vs Dogs",
    page_icon="🐶🐱",
    layout="wide"
)

# ======================================================
# 2️⃣ CẤU HÌNH MODEL (LIÊN QUAN MODEL)
# ======================================================

MODEL_FILENAME = "final_model.keras"  # file model CNN đã train
DEFAULT_IMAGE_SIZE = 128              # kích thước ảnh khi train
THRESHOLD = 0.5                       # ngưỡng cho sigmoid output

# ======================================================
# 3️⃣ LOAD MODEL (MODEL LOGIC)
# ======================================================

@st.cache_resource                    # cache để load model 1 lần
def load_model(model_path: str):
    """
    Load model Keras từ file
    """
    return tf.keras.models.load_model(model_path)

# ======================================================
# 4️⃣ TIỀN XỬ LÝ ẢNH (MODEL LOGIC)
# ======================================================

def preprocess(pil_img: Image.Image, image_size: int) -> np.ndarray:
    """
    Chuẩn hoá ảnh giống lúc train:
    - RGB
    - resize về IMAGE_SIZE x IMAGE_SIZE
    - chia /255
    - thêm batch dimension
    """
    img = pil_img.convert("RGB").resize((image_size, image_size))
    x = np.array(img).astype(np.float32) / 255.0
    x = np.expand_dims(x, axis=0)  # (1, H, W, 3)
    return x

# ======================================================
# 5️⃣ DỰ ĐOÁN (MODEL LOGIC)
# ======================================================

def infer(model, x: np.ndarray):
    """
    Chạy model và suy ra nhãn:
    - Sigmoid (1 neuron): binary classification
    - Softmax (2 neuron): cat vs dog
    """
    y = model.predict(x, verbose=0)

    # ===== Sigmoid output =====
    if y.shape[-1] == 1:
        p_dog = float(y[0][0])          # xác suất DOG
        p_cat = 1.0 - p_dog
        label = "DOG 🐶" if p_dog >= THRESHOLD else "CAT 🐱"
        conf = max(p_cat, p_dog)
        return label, conf, p_cat, p_dog, "sigmoid(1)"

    # ===== Softmax output =====
    if y.shape[-1] == 2:
        p_cat = float(y[0][0])
        p_dog = float(y[0][1])
        label = "DOG 🐶" if p_dog >= p_cat else "CAT 🐱"
        conf = max(p_cat, p_dog)
        return label, conf, p_cat, p_dog, "softmax(2)"

    raise ValueError(f"Output không hỗ trợ: {y.shape}")

# ======================================================
# 6️⃣ KIỂM TRA & LOAD MODEL (MODEL + UI)
# ======================================================

st.title("🐶🐱 Cats & Dogs: Image Classification")  # UI
st.header("📥 Upload & Dự đoán")

image_size = st.number_input(
        "IMAGE_SIZE",
        min_value=32,
        max_value=512,
        value=DEFAULT_IMAGE_SIZE,
        step=16
    )

uploaded = st.file_uploader(
        "Chọn ảnh (jpg/png)",
        type=["jpg", "jpeg", "png"]
    )

predict_btn = st.button(
        "Dự đoán",
        type="primary",
        disabled=(uploaded is None)
    )

model_path = Path(MODEL_FILENAME)
if not model_path.exists():
    st.error("❌ Không tìm thấy file model")  # UI feedback
    st.stop()

model = load_model(str(model_path))        # MODEL

# ======================================================
# 7️⃣ SESSION STATE
#    (GIỮ KẾT QUẢ SAU KHI BẤM NÚT)
# ======================================================

if "pred" not in st.session_state:
    st.session_state.pred = None


# ======================================================
# 8️⃣ CHIA GIAO DIỆN 2 CỘT (UI)
# ======================================================

left, right = st.columns([1, 1.2], gap="small")

# ======================================================
# 9️⃣ CỘT TRÁI – HIỂN THỊ ẢNH (UI)
# ======================================================

with left:
    st.header("🖼️ Ảnh được upload:")

    if uploaded:
        st.image(Image.open(uploaded), use_container_width=True)
    else:
        st.info("Hãy upload ảnh ở phía trên.")

# ======================================================
# 🔟 CỘT PHẢI – HIỂN THỊ KẾT QUẢ (UI)
# ======================================================

with right:
    st.header("🔮 Kết quả")

    # A) Nếu vừa bấm nút -> chạy dự đoán và lưu vào session_state
    if predict_btn and uploaded:
        pil_img = Image.open(uploaded)
        x = preprocess(pil_img, int(image_size))
        st.session_state.pred = infer(model, x)

    # B) Nếu đã có kết quả trong session_state -> hiển thị
    if st.session_state.pred and uploaded:
        label, conf, p_cat, p_dog, head = st.session_state.pred

        st.markdown(f"## {label}")
        st.write(f"Độ tin cậy: **{conf:.2%}**")

        st.progress(min(max(p_cat, 0.0), 1.0), text=f"CAT 🐱: {p_cat:.2%}")
        st.progress(min(max(p_dog, 0.0), 1.0), text=f"DOG 🐶: {p_dog:.2%}")

        st.session_state.pred = None # Reset lại kết quả dự đoán
    else:
        st.warning("Nhấn **Dự đoán** để xem kết quả.")
