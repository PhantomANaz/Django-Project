# Django-Project
Janata Wifi: Full Stack Developer Test<br>
It was my first experience with Django and it was slightly challenging, but I learned a lot along the way. I encountered difficulties, such as struggling with the integrated terminal in Visual Studio Code, which I eventually resolved by watching a helpful YouTube video. This project also allowed me to reuse my knowledge of Git, which I had been wanting to do for a while.<br>

The major challenge I faced was while dealing with 15000+ data in json file which at one point I needed to delete manually since I missed a field ('date'). Every time I was only able to delete 100 data which was both time-consuming and frustrating. After much Google Searching (to escape from deleting it manually) and deleting about 6k data (manually), I got the solution of using <b>DATA_UPLOAD_MAX_NUMBER_FIELDS</b> in <i>settings.py</i> which I set it to <b>10000</b> since its default value is 100.<br>
<br>
<b><u>Link:</u></b>
<ol>
<li>Table Visualization: http://127.0.0.1:8000/home/</li>
<li>Edit the Data: http://127.0.0.1:8000/edit_stock/16000/</li>
  <ul>
    <li>Here 16000 can be from 15934 to 63732</li>
  </ul>
</ol>

