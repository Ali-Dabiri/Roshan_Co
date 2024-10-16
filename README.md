# Roshan_Co

            <div id="content"><div style="text-align: right; direction: rtl;"> 
<li>1403/07/15</li>
</div>
<ul>
<li>مرتب کردن و درست کردن فایل های لازم مانند: Documentation جهت شروع کار</li>
<li>تحقیقات و مطالعه اولیه درباره requirement هر یک از task ها</li>
<li>شروع پروژه<ul>
<li>ایجاد virtualenv با نام Task_Roshan_RahkarPardazeshZharf.</li>
<li>ر pip install Django</li>
<li>ر pip install djangorestframework</li>
<li>مطالعه اجمالی Django<ul>
<li>کلیات و تاریخچه و کابردها</li>
<li>ر MVT model</li></ul></li>
<li>ر Create Project (Taknews)</li>
<li>Create app (newspage)</li></ul></li>
</ul>

<div style="text-align: right; direction: rtl;"> 
<li>1403/07/16</li>
</div>
<ul>
<li>ادامه پروژه (task01)<ul>
<li>ساخت و پیکربندی Views</li>
<li>ساخت و پیکربندی urls</li>
<li>ساخت templates و فایل NewsText.html</li>
<li>ساخت model با column های ذکر شده</li>
<li>مقدار دهی column های تعریف شده به طریق shell<ul>
<li>ر (py manage.py shell -i python)</li>
<li>ر News_Table.objects.create</li></ul></li>
<li>تکمیل فایل NewsText.html </li>
<li>ر Modify View </li>
<li>تحقیقات و مطالعه بیشتر درباره rest API، serializer و پیاده سازی آنها</li>
<li>تحقیقات و مطالعه موردی درباره serializer</li>
<li>ایجاد serializers.py </li>
<li>ر Modify view.py به خاطر افزودن serializer و برگرداندن لیست اخبار</li>
<li>ر Modify urls.py / ر ()as.view</li>
<li>مطالعه درباره QuerySet ها</li>
<li>ر Modify view.py / پیاده سازی فیلتر اخبار بر اساس تگ ها</li></ul></li>
</ul>
<div style="text-align: right; direction: rtl;"> 
<li>1403/07/17</li>
</div>
<ul>
<li>ر Modify view.py / پیاده سازی فیلتر اخبار بر اساس یک یا چند کلیدواژه موجود در متن و عنوان خبر</li>
<li>ر Modify view.py <ul>
<li>پیاده سازی فیلتر اخبار بر اساس عدم وجود کلیدواژه های خاص در متن و عنوان خبر </li>
<li>منتج به اعمال فیلترهای بخش 4 و 5 task به طور همزمان</li></ul></li>
<li>تحقیقات و مطالعه بیشتر درباره uni test نویسی</li>
<li>ایجاد tests.py و نوشتن unit test</li>
</ul>
<div style="text-align: right; direction: rtl;"> 
<li>1403/07/18</li>
</div>
<ul>
<li>تحقیقات و مطالعه درباره Web Scraping و Scrapy و متعلقات</li>
<li>شروع (task02)</li>
<li>ایجاد virtuelenv با نام Task_Roshan_RahkarPardazeshZharf_Task02.</li>
<li>ر pip install scrapy</li>
<li>ر Create Project Scrapy (Zoomit_Scraper)</li>
<li>مطالعه بیشتر درباره scrapy</li>
<li>ر ایجاد spider برای scrapy</li>
<li>ایجاد و پیاده سازی یک scraper ساده از صفحه <a href="https://www.zoomit.ir/featured-articles/427723-len-sassaman-satoshi-nakamoto-bitcoin/">https://www.zoomit.ir/featured-articles/427723-len-sassaman-satoshi-nakamoto-bitcoin/</a> <ul>
<li>استخراجات کدهای HTML / CSS مورد نیاز در این Scraper</li>
<li>ر scrapy crawl zoomit_news -o zoomit_news_data.json</li></ul></li>
<li>حضور در جلسه /// (میزبان جلسه حاضر نشد.) </li>
</ul>
<div style="text-align: right; direction: rtl;"> 
<li>1403/07/19</li>
</div>
<ul>
<li>تحقیقات و مطالعه اولیه درباره requirement هر یک از task03</li>
<li>شروع (task03)</li>
<li>ایجاد virtuelenv با نام Task_Roshan_RahkarPardazeshZharf_Task03.</li>
<li>ر pip install scrapy</li>
<li>ر Create Project Scrapy (Reuters_Gold_Scrapy)</li>
<li>ر scrapy genspider Reuters_Spider reuters.com</li>
<li>مطالعه بیشتر درباره timedelta, strptime</li>
<li>پیاده سازی اولیه (task03) </li>
</ul>
<div style="text-align: right; direction: rtl;"> 
<li>1403/07/20</li>
</div>
<ul>
<li>مطالعه بیشتر درباره xpath, data-testid</li>
<li>مطالعه و تست بابت (عدم نمایش response.url سایت Reuters) / نتیجه: ناموفق، و متوجه نشدن دلیل آن<ul>
<li>اقدامات صورت گرفته<ul>
<li>تست url صفحه search</li>
<li>تست url یکی از صفحات نتایج search شده</li>
<li>تست url آخرین خبر منتشر شده در سایت Reuters</li>
<li>تست url خود سایت Reuters / ر <a href="https://www.reuters.com/">https://www.reuters.com/</a></li>
<li>ر ROBOTSTXT_OBEY = False در settings.py و تست دوباره مراحل و url های ذکر شده در بالا</li>
<li>غیرفعال کردن AdBlocker extension و تست دوباره مراحل و url های ذکر شده در بالا</li>
<li>ر register کردن در سایت Reuters و تست دوباره مراحل و url های ذکر شده در بالا</li></ul></li></ul></li>
<li>بازنویسی و تست و ساده سازی برنامه با سایت ISNA </li>
<li>توسعه برنامه با سایت ISNA</li>
<li>ایجاد و پیاده سازی (task03) با سایت KhabarOnline</li>
<li>ساخت دوباره یک virtualven و انجام مراحل کلیدی قبل برای مرتب و تمیز کردن (task03)</li>
</ul>
<div style="text-align: right; direction: rtl;"> 
<li>1403/07/22</li>
</div>
<ul>
<li>ر Create و push branch کردن task های انجام شده در github و merge کردن آنها</li>
<li>ر Create Account pythonanywhere و Deploy کردن پروژه <ul>
<li>ر <a href="https://alid.pythonanywhere.com/api/News_Page/">https://alid.pythonanywhere.com/api/News_Page/</a></li></ul></li>
<li>حضور در جلسه </li>
<ul>
<li>ر selenium برای task02 , 03</li></ul>
</ul>
<div style="text-align: right; direction: rtl;"> 
<li>1403/07/23</li>
</div>
<ul>
<li>دوباره نویسی (task02) از اول</li>
<li>ر Create virtualenv / ر Task_Roshan_RahkarPardazeshZharf_Task02.<ul>
<li>ر pip install Django</li>
<li>ر pip install djangorestframework</li>
<li>ر pip install selenium</li>
<li>ر pip install scrapy</li></ul></li>
<li>ر Create Project Scrapy<ul>
<li>ر scrapy startproject Zoomit_Scrapy</li>
<li>ر scrapy genspider Zoomit_Spider zoomit.ir</li></ul></li>
<li>نوشتن برنامه برای تست گرفتن url صفحه مورد نظر zoomit<ul>
<li>خواندن robots.txt سایت zoomit<ul>
<li>ر <a href="https://www.zoomit.ir/robots.txt">https://www.zoomit.ir/robots.txt</a></li></ul></li>
<li>ر ROBOTSTXT_OBEY = False در settings.py </li>
<li>تست مجدد و دریافت url صفحه مورد نظر zoomit و عدم دریافت محتوای داخل tag مورد نظر </li></ul></li>
<li>تحقیقات و مطالعه بیشتر درباره ...<ul>
<li>ر selenuim</li>
<li>ر xpath </li>
<li>ر dynamic page</li></ul></li>
<li>ر pip install webdriver-manager</li>
<li>نوشتن برنامه برای تست نصب webdriver, selenium و در کل ChromeDriver</li>
<li>نوشتن برنامه scraper از صفحه مورد نظر </li>
<ul>
<li>آدرس صفحه مورد نظر: https://www.zoomit.ir/search/news/</li></ul>
</ul>
<div style="text-align: right; direction: rtl;"> 
<li>1403/07/25</li>
</div>
<ul>
<li>دوباره نویسی (task03) از اول</li>
<li>ر Create virtualenv / ر Task_Roshan_RahkarPardazeshZharf_Task03.<ul>
<li>ر pip install Django</li>
<li>ر pip install djangorestframework</li>
<li>ر pip install selenium</li>
<li>ر pip install scrapy</li>
<li>ر pip install webdriver-manager</li></ul></li>
<li>ر Create Project Scrapy<ul>
<li>ر scrapy startproject Reuters_Scrapy</li>
<li>ر scrapy genspider Reuters_Spider Reuters.com</li></ul></li>
<li>نوشتن برنامه برای تست گرفتن url صفحه مورد نظر reuters<ul>
<li>خواندن robots.txt سایت reuters<ul>
<li>ر <a href="https://www.reuters.com/robots.txt">https://www.reuters.com/robots.txt</a></li></ul></li>
<li>ر ROBOTSTXT_OBEY = False در settings.py </li></ul></li>
<li>تحقیقات و مطالعه بیشتر درباره ...<ul>
<li>ر WebDriverWait</li>
<li>ر selenium.webdriver.common.by</li>
<li>ر expected_conditions</li>
<li>ر add_argument<ul>
<li>ر user-agent<ul>
<li>ر <a href="https://www.useragentstring.com/">https://www.useragentstring.com/</a></li></ul></li></ul></li></ul></li>
<li>نوشتن برنامه برای تست url صفحه مورد نظر </li>
<li>مطالعه بیشتر درباره حل مشکل captcha با کمک cookies ها</li>
<li>حضور در جلسه </li>
<ul>
<li>ارائه task 01, 02, 03</li></ul>
</ul>
</div>
