class datasettoimport(object):
    """docstring for data"""

    # def __init__(self, arg):
    #     super(data, self).__init__()
    # self.arg = arg

    # platform = ['宜人', '陆金']
    ratingorganization = '网贷天眼'
    rating = [
        ['宜人贷', '1', 'http://yirendai.p2peye.com'],
        ['拍拍贷', '2', 'http://ppdai.p2peye.com'],
        ['陆金服', '3', 'http://lu.p2peye.com'],
        ['人人贷', '4', 'http://we.p2peye.com'],
        ['宜贷网', '5', 'http://yidai.p2peye.com'],
        ['开鑫金服', '6', 'http://gkkxd.p2peye.com'],
        ['微贷网', '7', 'http://weidai.p2peye.com'],
        ['投哪网', '8', 'http://touna.p2peye.com'],
        ['小赢理财', '9', 'http://xiaoying.p2peye.com'],
        ['点融网', '10', 'http://dianrong.p2peye.com'],
        ['凤凰金融', '11', 'http://fengjr.p2peye.com'],
        ['有利网', '12', 'http://yooli.p2peye.com'],
        ['团贷网', '13', 'http://tuandai.p2peye.com'],
        ['翼龙贷', '14', 'http://eloancn.p2peye.com'],
        ['麻袋理财', '15', 'http://madailicai.p2peye.com'],
        ['海融易', '16', 'http://hairongyi.p2peye.com'],
        ['积木盒子', '17', 'http://jimubox.p2peye.com'],
        ['爱钱进', '18', 'http://iqianjin.p2peye.com'],
        ['鑫合汇', '19', 'http://xinhehui.p2peye.com'],
        ['你我贷', '20', 'http://niwodai.p2peye.com'],
        ['小牛在线', '21', 'http://xiaoniu88.p2peye.com'],
        ['和信贷', '22', 'http://hexindai.p2peye.com'],
        ['Ppmoney', '23', 'http://ppmoney.p2peye.com'],
        ['东方汇', '24', 'http://eastlending.p2peye.com'],
        ['民贷天下', '25', 'http://mindai.p2peye.com'],
        ['道口贷', '26', 'http://daokoudai.p2peye.com'],
        ['银湖网', '27', 'http://yinhu.p2peye.com'],
        ['财富星球', '28', 'http://caifuxq.p2peye.com'],
        ['博金贷', '29', 'http://bjdp2p.p2peye.com'],
        ['金开贷', '30', 'http://jkd.p2peye.com'],
        ['人人聚财', '31', 'http://rrjc.p2peye.com'],
        ['融金所', '32', 'http://rjs.p2peye.com'],
        ['理财范', '33', 'http://licaifan.p2peye.com'],
        ['玖融网', '34', 'http://jiurong.p2peye.com'],
        ['生菜金融', '35', 'http://shengcaijinrong.p2peye.com'],
        ['北京众信金融', '36', 'http://imzhongxin.p2peye.com'],
        ['短融网', '37', 'http://duanrong.p2peye.com'],
        ['友金所', '38', 'http://yyfax.p2peye.com'],
        ['银豆网', '39', 'http://yindou.p2peye.com'],
        ['首金网', '40', 'http://shoujinwang.p2peye.com'],
        ['恒大金服', '41', 'http://hdfax.p2peye.com'],
        ['广信贷', '42', 'http://guangxindai.p2peye.com'],
        ['链链金融', '43', 'http://lljr.p2peye.com'],
        ['付融宝', '44', 'http://frbao.p2peye.com'],
        ['拓道金服', '45', 'http://51tuodao.p2peye.com'],
        ['铜掌柜', '46', 'http://tzg.p2peye.com'],
        ['爱钱帮', '47', 'http://iqianbang.p2peye.com'],
        ['广州e贷', '48', 'http://gzdai.p2peye.com'],
        ['红岭创投', '49', 'http://my089.p2peye.com'],
        ['联金所', '50', 'http://uf-club.p2peye.com'],
        ['口袋理财', '51', 'http://koudailc.p2peye.com'],
        ['图腾贷', '52', 'http://tutengdai.p2peye.com'],
        ['向上金服', '53', 'http://xiangshang360.p2peye.com'],
        ['理想宝', '54', 'http://id68.p2peye.com'],
        ['米缸金融', '55', 'http://migang.p2peye.com'],
        ['e融所', '56', 'http://myerong.p2peye.com'],
        ['联连理财', '57', 'http://lianlianmoney.p2peye.com'],
        ['奇乐融', '58', 'http://qilerong.p2peye.com'],
        ['鹏金所', '59', 'http://penging.p2peye.com'],
        ['腾邦创投', '60', 'http://p2p178.p2peye.com'],
        ['汉金所', '61', 'http://hanxinbank.p2peye.com'],
        ['万盈金融', '62', 'http://wyjr168.p2peye.com'],
        ['中瑞财富', '63', 'http://zrcaifu.p2peye.com'],
        ['抱财网', '64', 'http://baocai.p2peye.com'],
        ['果树财富', '65', 'http://goodsure.p2peye.com'],
        ['可溯金融', '66', 'http://kesucorp.p2peye.com'],
        ['e路同心', '67', 'http://88bank.p2peye.com'],
        ['珠宝贷', '68', 'http://zhubaodai.p2peye.com'],
        ['永利宝', '69', 'http://yonglibao.p2peye.com'],
        ['合拍在线', '70', 'http://he-pai.p2peye.com'],
        ['钜宝盆', '71', 'http://jpjbp.p2peye.com'],
        ['看看钱包', '72', 'http://kkqb.p2peye.com'],
        ['立业贷', '73', 'http://liyedai.p2peye.com'],
        ['金联储', '74', 'http://jinlianchu.p2peye.com'],
        ['沪商财富', '75', 'http://hushangcaifu.p2peye.com'],
        ['杉易贷', '76', 'http://33lend.p2peye.com'],
        ['华人金融', '77', 'http://hrj5262.p2peye.com'],
        ['91旺财', '78', 'http://91wangcai.p2peye.com'],
        ['新联在线', '79', 'http://newunion.p2peye.com'],
        ['信用宝', '80', 'http://xyb100.p2peye.com'],

    ]