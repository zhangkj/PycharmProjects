# -*- coding:utf-8 -*-
import  re


str = """

<div class="article block untagged mb15" id='qiushi_tag_115478565'>

<div class="author clearfix">
<a href="/users/30843538" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3084/30843538/medium/20151225073126.jpg" alt="巨魔帮帮主"/>
</a>
<a href="/users/30843538" target="_blank" title="巨魔帮帮主">
<h2>巨魔帮帮主</h2>
</a>
</div>


<div class="content">

第一名和第二名是对手，但倒数第一和倒数第二往往是朋友。你们呢？
<!--1457691009-->

</div>



<div class="stats">
<span class="stats-vote"><i class="number">14893</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/115478565" data-share="/article/115478565" id="c-115478565" class="qiushi_comments" target="_blank">
<i class="number">250</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_115478565" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-115478565" class="up">
<a href="javascript:voting(115478565,1)" class="voting" data-article="115478565" id="up-115478565" rel="nofollow">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">15232</span>
</a>
</li>
<li id="vote-dn-115478565" class="down">
<a href="javascript:voting(115478565,-1)" class="voting" data-article="115478565" id="dn-115478565" rel="nofollow">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-339</span>
</a>
</li>

<li class="comments">
<a href="/article/115478565" id="c-115478565" class="qiushi_comments" target="_blank">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a href="###" class="jiathis_button_weixin" rel="external nofollow"></a>
<a href="###" class="jiathis_button_cqq" rel="external nofollow"></a>
<a href="###"class="jiathis_button_qzone" rel="external nofollow"></a>
<a href="###" class="jiathis_button_tsina" rel="external nofollow"></a>
<a href="###" class="jiathis_button_tieba" rel="external nofollow"></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank" rel="external nofollow"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>

</div>

"""
pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats">.*?number">(.*?)</i>.*?number">(.*?)</i>',re.S)

items = re.findall(pattern,str)
print len(items)
print items