import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import re
from datetime import datetime, timedelta

# 加载图片
image_path = '2.jpg'
image = Image.open(image_path)

gray_image = image.convert('L')

# 增强对比度
enhancer = ImageEnhance.Contrast(gray_image)
enhanced_image = enhancer.enhance(2.0)


# 使用 Tesseract OCR 读取图片中的文本
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'  # 根据你安装的位置调整路径
text = pytesseract.image_to_string(enhanced_image)

# 正则表达式匹配日期和时间段
date_pattern = r'(\d{4})[年\-](\d{1,2})[月\-](\d{1,2})'  # 匹配日期格式：2023年06月25日或2023-06-25
time_pattern = r'(\d{1,2}:\d{2})'  # 匹配时间格式，例如08:42

date_match = re.search(date_pattern, text)
time_matches = re.findall(time_pattern, text)

if date_match:
    year, month, day = map(int, date_match.groups())
    work_date = datetime(year, month, day)
    print(f"日期: {work_date.strftime('%Y-%m-%d')}")
else:
    print("未找到日期信息。")

# 计算工作时长
if time_matches:
    times = [datetime.strptime(t, '%H:%M') for t in time_matches]
    breakpoint()
    work_duration = timedelta()
    for i in range(1, len(times), 2):
        if i + 1 < len(times):
            start_time = times[i]
            end_time = times[i + 1]
            work_duration += (end_time - start_time)
    
    total_seconds = work_duration.total_seconds()
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    print(f"工作时长: {int(hours)}小时{int(minutes)}分钟")
else:
    print("未找到时间信息。")