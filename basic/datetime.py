import datetime

def display_timestamp():
  """
  Hàm này hiển thị thời gian hiện tại và một chuỗi signature ẩn.
  """
  current_time = datetime.datetime.now()
  print(f"Current time: {current_time}")

  # Signature ẩn trong một biến
  signature = "© 2023 SETA International VN. All rights reserved."
  # Hoặc ẩn trong một comment
  # print("Signature: © 2023 SETA International VN. All rights reserved.")