#记录所有的名片字典
card_list=[]

def show_menu():
    print("*"* 50)
    print("欢迎使用[名片管理系统] V 1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*"*50)

def new_card():
    """新增名片"""
    #1.提示用户输入名片的详细信息
    name_str=input("请输入姓名: ")
    phone_str =input("请输入电话: ")
    QQ_str=input("请输入QQ: ")
    email_str=input("请输入email: ")

    #建立名片字典
    card_dict={"name":name_str,
               "phone":phone_str,
               "QQ":QQ_str,
               "email":email_str}
    #3.将字典名片添加的列表中
    card_list.append(card_dict)
    print(card_list)
    #4.提示用户添加成功
    print("添加 %s 的名片成功" % name_str)
    print("-"*50)
    print("新增名片")

def show_all():
    if len(card_list)==0:
        print("当前无任何记录,请使用新增功能增加名片:")
        return
    print("-"*50)
    print("显示所有名片")
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t"*2)
    print("")
    print("="*50)

    #遍历名片列表,依次输出名片信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],card_dict["phone"],
              card_dict["QQ"],card_dict["email"]))
    print("")
def search_card():
    print("-"*50)
    print("搜索名片")
    #1.提示用户要搜索的姓名
    find_name=input("请输入要搜索的姓名: ")

    #2.遍历名片列表
    for card_dict in card_list:
        if card_dict["name"]==find_name:
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t" * 2)
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"], card_dict["phone"],
                                                card_dict["QQ"], card_dict["email"]))
            print("")
            deal_card(card_dict)
            break
    else:
        print("抱歉,没找到 %s " % find_name)
def deal_card(find_dict):
    print(find_dict)
    action_str=input("请选择要执行的操作 "
                     "[1] 修改 [2] 删除 [0] 返回上级菜单")
    if action_str=="1":
        find_dict["name"]=input_card_info(find_dict["name"],"姓名: ")
        find_dict["phone"]=input_card_info(find_dict["phone"],"电话: ")
        find_dict["QQ"]=input_card_info(find_dict["QQ"],"QQ: ")
        find_dict["email"]=input_card_info(find_dict["email"],"email: ")
        print("修改名片")

    elif action_str=="2":
        print("删除名片")
        card_list.remove(find_dict)
        print("删除名片成功!")

def input_card_info(dict_value,tip_message):
    """输入名片信息

    :param dict_value: 字典原有值
    :param tip_message: 提示信息
    :return:
    """
    result_str=input(tip_message)
    if len(result_str)>0:
        return result_str
    else:
        return dict_value