?????
1.url?https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=0
2.post? first=false&pn=2&kd=python
3.cookie
	user_trace_token=20171021105642-7782f85f-b60b-11e7-95b8-5254005c3644
	LGUID=20171021105642-7782fc28-b60b-11e7-95b8-5254005c3644
	index_location_city=%E4%B8%8A%E6%B5%B7
	JSESSIONID=ABAAABAAAFCAAEG6C94FE41548F92A1A52584E87B1DB3F1
	PRE_UTM=
	PRE_HOST=
	PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F
	PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D
	_gat=1
	SEARCH_ID=be266038293d4c2ea9533d6fc54c8667
	_gid=GA1.2.702331301.1508994525
	Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508731882,1508731894,1508855710,1508994525
	Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508994829
	_ga=GA1.2.1112443934.1508554591
	LGSID=20171026130917-d14ab657-ba0b-11e7-a8ed-525400f775ce
	LGRID=20171026131347-72424af8-ba0c-11e7-9625-5254005c3644
	TG-TRACK-CODE=search_code


?????
https://www.lagou.com/jobs/{positionId}.html
//div[@class='job-name']/span[@class='name']????
//span[@class='salary']??
//dd[@class='job_request']/p[1]/span[3]????
//dd[@class='job-advantage']/p????
//dd[@class='job_bt']//p[1]????
//dd[@class='job_bt']//p[2]????

?????????/br/following::text()[1]??br????????
content = etree.HTML(html.content)
result = content.xpath("//dd[@class='job_bt']//p[1]/br/following::text()[1]")print(result)



???
job_name = content.xpath("//div[@class='job-name']/span[@class='name']")
job_salary = content.xpath("//span[@class='salary']")
job_experience = content.xpath("//dd[@class='job_request']/p[1]/span[3]")
print(job_experience[0].text)
job_advantage = content.xpath("//dd[@class='job-advantage']/p")
print(job_advantage[0].text)
responsibility = content.xpath("//dd[@class='job_bt']//p[1]/br/following::text()[1]")
claim = content.xpath("//dd[@class='job_bt']//p[2]/br/following::text()[1]")
claim = str()
for i in result:
    claim += i.replace(r'\xa0', '')
print(claim)



???????
</script>

    <!-- ???? -->    <!-- ??token???????????? -->
    <script type="text/javascript">
    window.X_Anti_Forge_Token = '2022a583-3cb2-47dd-b0a3-99558a46f7a0';
    window.X_Anti_Forge_Code = '72836060';
</script>


'Connection':' keep-alive',
'Content-Length':' 25',
'Origin':' https://www.lagou.com',
'X-Anit-Forge-Code':' 0',
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
'Accept':' application/json, text/javascript, */*; q=0.01',
'X-Requested-With':' XMLHttpRequest',
'X-Anit-Forge-Token':' None',
'Referer':' https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
'Accept-Encoding':' gzip, deflate, br',
'Accept-Language':' zh-CN,zh;q=0.8',
'Cookie':' user_trace_token=20171021105642-7782f85f-b60b-11e7-95b8-5254005c3644; LGUID=20171021105642-7782fc28-b60b-11e7-95b8-5254005c3644; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.702331301.1508994525; _ga=GA1.2.1112443934.1508554591; LGRID=20171026141942-a79f8d3b-ba15-11e7-a8ff-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508731882,1508731894,1508855710,1508994525; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508998784; TG-TRACK-CODE=search_code; JSESSIONID=ABAAABAAAFCAAEG6C94FE41548F92A1A52584E87B1DB3F1; SEARCH_ID=428d311fe8bf4cf6b9c55ebdef9f9f18',



???headers???

