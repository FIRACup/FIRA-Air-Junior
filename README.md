# FIRA-Air-U19


# <div dir="rtl">راهنمای فارسی نصب واستفاده از ربات Tello</div>

<div dir="rtl">
  برای برنامه نویسی به زبان پایتون و کنترل خودکار ربات Tello باید سه مرحله را به انجام برسانید:
<br>
<br>
  1- بر روی یک لپتاپ مجهز به سیستم عامل لینوکس (ترجحا نسخه Ubuntu 18.04) کتابخانه پردازش تصویر Opencv را نصب نمایید.
<br>
2- کتابخانه نشانگر یا Marker مورد نظر خود برای تشخیص دروازه ها را نصب کنید.<br>
3- SDK مربوط به Tello را نصب نمایید و لپتاپ را به ربات متصل کنید. برای اطمینان از نصب صحیح میتوانید نمونه کدهای موجود در این بروژه را اجرا کنید. 
  <br>
  <br>
  بعد از طی کردن این مراحل، شما میتوانید تصویر دوربین ربات را از طریق شبکه بی سیم دریافت و پردازش کنید و از طریق برنامه نویسی پایتون فرمانهای کنترلی مناسب را به ربات ارسال نمایید.
  <br>
  <br>
  
  راهنمای جزئی مراحل نصب کتابخانه opencv در این لینک قابل دریافت است:
  <br>
  https://docs.google.com/document/d/1bhRKXJmQ7LDGyPqWj91_aCIEldzdO1PBxEqAiDd_q00/edit?usp=sharing
  <br>
  <br>
  برای نصب SDK ربات Tello مراحل زیر را طی نمایید:
  <br>
  <br>
این راهنما برای نسخه پایتون 3.6 و SDK نسخه 0.6 ربات Tello بر روی سیستم عامل Ubuntu 18.04 تست شده است. جهت جلوگیری از مشکلات احتمالی، استفاده از نسخه مشابه توصیه می شود.
<br>
<br>
بافرض اینکه سیستم عامل لینوکس Ubuntu 18.04  را به تازگی نصب کرده اید مراحل زیر را طی نمایید: 
<br>
<br>
1- ابتدا به اینترنت متصل شوید. برای نصب نرم افزار در سیستم عامل لینوکس اتصال به اینترنت ضروری است. سپس محیط ترمینال را باز کرده (Ctrl+Alt+t) و دستورات زیر را یکی یکی درآن اجرا نمایید:

</div>

```
sudo apt update
sudo apt install python3-pip
sudo apt install git
sudo apt install pkg-config
sudo apt install libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libavfilter-dev  libswscale-dev libswresample-dev
sudo apt install mplayer
```

<div dir="rtl">
  دستورات بالا نرم افزار های جانبی مورد نیاز را بر روی سیستم نصب می کند.
  <br>
  <br>
  2- کتابخانه های ضروری پایتون را از طریق وارد کردن دستورهای زیر در ترمینال، نصب نمایید: 
</div>

```
sudo pip3 install av
sudo pip3 install opencv-python  (if not installed! If you have previously installed it, skip this command)
sudo pip3 install image
sudo pip3 install pygame
```

<div dir="rtl">
 3-  پس از نصب ابزارهای مورد نیاز، میتوانید SDK ربات Tello را نصب نمایید. کافیست دستورات زیر را در ترمینال وارد نمایید:
</div>

```
git clone https://github.com/hanyazou/TelloPy
cd TelloPy
python setup.py bdist_wheel
pip install dist/tellopy-*.dev*.whl --upgrade
```

<div dir="rtl">
  اکنون می توانید از طریق برنامه نویسی پایتون به تصویر دوربین ربات به صورت بی سیم دسترسی داشته باشید و فرمانهای کنترلی را به آن ارسال نمایید. برای اجرای مثالها و کنترل ربات:
  <br>
  <br>
  ابتدا باید ربات را روشن کنید، بعد از 10 ثانیه لپتاپ را به وای فای ربات متصل کنید.
  <br>
  کد مثال را در ترمینال از طریق دستور python3 sampleCode.py اجرا کنید(به جای sampleCode نام و مسیر واقعی کد مد نظر را بنویسید)
  <br>
  <br>
  
  توجه داشته باشید در صورتی که ربات تلو را روشن کنید و مدتی بر روی زمین در دمای اتاق قرار دهید، به دلیل گرم شدن پردازنده پس از چند دقیقه به صورت خودکار خاموش خواهد شد.
  <br>
  برای جلوگیری از خاموش شدن در جای ثابت لازم است ربات را خنک نمایید (به عنوان نمونه، با استفاده از یک فن کوچک). در زمان پرواز، پردازنده به صورت طبیعی خنک خواهد شد و خاموشی خودکار اتفاق نخواهد افتاد.
</div>
