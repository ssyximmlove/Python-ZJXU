import random

first_names = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁"
last_names = "一丁七万丈三上下丑丐不专且丕世丘丙业丛东丝丞丢两严丧个临丸丹为主丽举乃久么义之乌乍乎乏乐乒乓乔乖乘乙九乞也习乡书买乱乳乾了予争事二于亏云互亓五井亚些亡交亦亨享京亭亮亲人亿什仁仂仃仄仅仆仇仉今介仍从仑仓仔仕他仗付仙代令以仨仪仫们兄兰冉内冈册再农冬冯冰冲决况冷凝凡凶凸凹出刀刁分划刊刑刘则刚创初删判刨利别力加功劣动助努励劲劳势勃勇勉勋勾勿匀包匆化北匙匠匣匪匹区医匿十千升午卉半华协卑卒卓单卖南博卜占卡卢卫印危即却卵卷卸卿厂厅历厉压厌厕厘厚原去县叁参又叉及友双反发叔取受变叙叠口古句另叨叩只叫召叭叮可台史右叶号司叹叼吃各合吉吊同名后吏吐向吓吕吗君吞吟否吧吨吩含听启吴吵吸吹吻呜呀呆呈告周味呼命咆咋和咖咬咯咱咳咸咻咽咪品哄哈响哎哑哒哗哥哦哧哨唐唠唤唧唬售唯唱唷唸唾啃啄商啊啡啤啥啦啪啬啭啮啸喂喜喷喻嗅嗓嗜嗡嗽嘛嘀嘉嘎器嚎嚏嚷嚼囊四回因团园困囱围固国图圆土圣在圭地场圾址均坊坎坏坐坑块坚坛坝坞坟坠坡坤坦坪坯坷垂垃垄型垒垓垛垠埋城域埠埤基堂堆堑堕堡堤堪堰堵塌塑塔塘塞填塬塾境墓墅墙增墟墨墩壁壤士壮声壳壶处备复夏夕外多夜够央失头夷夸夹夺女奴奶奸她好如妄妆妇妈妒妓妖妙妥妨妹妻姆姊始姐姑姓委姜姥姨姻姿威娃娄娇娘娱娶婆婉婚婶婿媒媚媳妇婷婿媛嫔婴嬲子孑孔孕字存孙孝孟季季孤学孩孪孬孰孵孽宁它宅宇守安宋完宏宗官宙定宛宜宝实实宠审客宣室宥宦宪宫宰害宴宵家容宽宾宿寂寄密寇富寒寓寝寞察寡寥寨寸对寺寻导寿封射将专尉尊小少尔尖尘尚尝尤就尸尺尼尽尾尿局屁层居屈屉届屋屎屏屑展属屠屡屿岁岂岖岗岛岩岭岳岸峡峰峻崇崎崔崖崩崭巍川州巡巢工左巧巨巩巫差己已巴巷巾币市布帅帆师希帐帕帖帘帚帜带帷常帽幅幕帮干平年并幸幻幼幽广庄庆庇床序底店庙庚府庞废度座库庭庵庶康庸廉廊廓廖延廷建开异弃弄式弓引弛张强弹归当录形彦彩彪彬彭彰影役彼往征径待很徊律後徐徒得徘徙徜御循微德徵心必忆忌忍忏忐忑忒志忘忙忠忧快念忽怒怕怖怜思怠怡急怦性怨怪怯总恃恋恐恒恕恢恤恨恩恪恬恭息恰恳恶恼悄悉悌悍悔悟悠患悦您悯悲悴悼情惊惋惕惜惟惠惦惧惨惩惫惭惮惯戚闷情想惶惹愁愈愉意愕愚爱感愧愿慈慑慕慢慧慨慰憋憎憔憨憾懂懈懊懒怀悬戒我或战戚截戮戳戴户房所扁扇手才扎扑扒打扔托扛扣执扩扫扬扭扮扯扰扶批找承技抄把抢折抒投抖抗抚护抹拨择抬抱抵押抽拐拍拒拓拔拗招披拥拴拾持挂指按挑挖挣挡挠挟括拭拯拱拳拴拷拼拽拾拿持挂指按挎挑挡挣拯挠挟括拭挠挡挟括拭拱拳拷拼拽挎挑挖挣挡挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱拳拷拼拽挎挑挖挣挡挠挟括拭拯拱"


def generate_student_info(num_students=6):
    classes = ['班级1', '班级2', '班级3']
    sexes = ['男', '女']
    student_info = []
    for i in range(num_students):
        name = f'{random.choice(first_names) + random.choice(last_names)}'
        sex = random.choice(sexes)
        cls = random.choice(classes)
        student_id = f'2024{random.randint(1000, 9999)}'
        student_info.append(f'{name},{sex},{cls},{student_id}')
    return student_info


def write_to_file(filename, student_info):
    with open(filename, 'w') as f:
        for info in student_info:
            f.write(info + '\n')


def read_and_output_file(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


if __name__ == "__main__":
    filename = 'student_info.txt'
    student_data = generate_student_info()
    write_to_file(filename, student_data)
    read_and_output_file(filename)
