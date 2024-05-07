import streamlit as st

st.title("Streamlit 超入門")

"""
---
## write

```python
#必要ライブラリ
import streamlit as st

st.write("DataFrame")
```
"""
st.write("DataFrame")


"""
---
## empty progress

```python
#必要ライブラリ
import streamlit as st
import time

latest_iteration = st.empty()　#空要素
bar = st.progress(0)　#プログレスバー定義
st.write(":::::::::")

for i in range(100):　#100回繰り返し処理
    latest_iteration.text(f"Iteration {i+1}")　#進行状況を１ずつ更新
    bar.progress(i + 1)　#プログレスバーを１ずつ更新
    time.sleep(0.01)　#繰り返しのたびに0.01止まる（0.01間隔で処理実行）
```
"""

import time

latest_iteration = st.empty()
bar = st.progress(0)
st.write(":::::::::")

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)


"""
---
## DataFrame

```python
#必要ライブラリ
import streamlit as st
import pandas as pd

df = pd.DataFrame({"1列目": [1, 2, 3, 4], "2列目": [10, 20, 30, 40]})

st.dataframe(df.style.highlight_max(axis=0))
```
"""
import pandas as pd

df = pd.DataFrame({"1列目": [1, 2, 3, 4], "2列目": [10, 20, 30, 40]})

st.dataframe(df.style.highlight_max(axis=0))

"""
---
## if checkbox Image.open

```python
#必要ライブラリ
import streamlit as st
from PIL import Image

if st.checkbox("Show Image"):　#チェックボックス
    img = Image.open("Streamlit.png")　#画像取得
    st.image(img, caption="Streamlit image", use_column_width=True)　#(画像取得, キャプション, 横幅に合わせてサイズを変更)
```
"""

from PIL import Image

if st.checkbox("Show Image"):
    img = Image.open("Streamlit.png")
    st.image(img, caption="Streamlit image", use_column_width=True)


"""
---
## selectbox

```python
#必要ライブラリ
import streamlit as st

option = st.selectbox("あなたの好きな数字を教えてください。", list(range(1, 11)))
"あなたの好きな数字は、", option, "です。"
```
"""

option = st.selectbox("あなたの好きな数字を教えてください。", list(range(1, 11)))
"あなたの好きな数字は、", option, "です。"

"""
---
## text_input

```python
#必要ライブラリ
import streamlit as st

text = st.text_input("あなたの趣味を教えてください。")
"あなたの趣味は、", text, "です。"
```
"""

text = st.text_input("あなたの趣味を教えてください。")
"あなたの趣味は、", text, "です。"

"""
---
## slider

```python
#必要ライブラリ
import streamlit as st

condition = st.slider("あなたの今の調子は？", 0, 100, 50)　#(ラベル, 最小値, 最大値, 初期値)
"コンディション：", condition
```
"""

condition = st.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション：", condition

"""
---
## sidebar

```python
#必要ライブラリ
import streamlit as st

st.sidebar.title("Sidebar")　#st.sidebar.~~

sidebarText = st.sidebar.text_input("あなたの特技を教えてください。")
st.sidebar.write("あなたの特技は、", sidebarText, "です。")
```
"""

st.sidebar.title("Sidebar")

sidebarText = st.sidebar.text_input("あなたの特技を教えてください。")
st.sidebar.write("あなたの特技は、", sidebarText, "です。")

"""
---
## columns

```python
#必要ライブラリ
import streamlit as st

left_column, right_column = st.columns(2)
left_button = left_column.button("右カラムに文字を表示")
if left_button:
    right_column.write("ここは右カラム")
```
"""

left_column, right_column = st.columns(2)
left_button = left_column.button("右カラムに文字を表示")
if left_button:
    right_column.write("ここは右カラム")


"""
---
## expander

```python
#必要ライブラリ
import streamlit as st

expander = st.expander("問い合わせ１")
expander.write("問い合わせ１の回答")
expander = st.expander("問い合わせ２")
expander.write("問い合わせ２の回答")
expander = st.expander("問い合わせ３")
expander.write("問い合わせ３の回答")
```
"""

expander = st.expander("問い合わせ１")
expander.write("問い合わせ１の回答")
expander = st.expander("問い合わせ２")
expander.write("問い合わせ２の回答")
expander = st.expander("問い合わせ３")
expander.write("問い合わせ３の回答")
