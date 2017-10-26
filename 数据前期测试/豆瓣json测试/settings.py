
filepath = 'douban_move_python.html'

headers = {
    'Connection':'keep-alive',
    # 'Content-Length':'25',
    # 'Origin':'https://www.lagou.com',
    # 'X-Anit-Forge-Code':'0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Accept':'application/json,text/javascript,*/*;q=0.01',
    # 'X-Requested-With':'XMLHttpRequest',
    # 'X-Anit-Forge-Token':'None',
    # 'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.8',
    # 'Cookie':'user_trace_token=20171021105642-7782f85f-b60b-11e7-95b8-5254005c3644; LGUID=20171021105642-7782fc28-b60b-11e7-95b8-5254005c3644; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.702331301.1508994525; _ga=GA1.2.1112443934.1508554591; LGRID=20171026141942-a79f8d3b-ba15-11e7-a8ff-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508731882,1508731894,1508855710,1508994525; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508998784; TG-TRACK-CODE=search_code; JSESSIONID=ABAAABAAAFCAAEG6C94FE41548F92A1A52584E87B1DB3F1; SEARCH_ID=428d311fe8bf4cf6b9c55ebdef9f9f18',
#
}
#
get_data = {
'type':'movie',
'tag':'豆瓣高分',
'page_limit':50,
'page_start':0,
}

post_data = {
    # 'first': 'false',
    # 'pn': 2,
    # 'kd': 'python',

}