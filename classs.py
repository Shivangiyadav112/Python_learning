# class WebSeries:
#     show_name = 'suites'
#     show_length = '180'

# WebSeries_obj = WebSeries()
# print(WebSeries_obj.show_name)
# print(WebSeries_obj.show_length)


class WebSeries:
    def __init__(self,name,season,episode):
        self.name = name
        self.season = season
        self.episode = episode

web1 = WebSeries('game of thrones',1,2)
web2 = WebSeries('suits',1,2)
print(web1.name,web2.name)
