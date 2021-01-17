"""
test
    {"HEAD_R":0,"BODY_Y":-1,"R_SHOU":-32,"HEAD_P":-11,"R_ELBO":0,"L_ELBO":0,"HEAD_Y":-8,"L_SHOU":-69},
    {"HEAD_R":0,"BODY_Y":-18,"R_SHOU":-32,"HEAD_P":-19,"R_ELBO":0,"L_ELBO":0,"HEAD_Y":35,"L_SHOU":-69},
    {"HEAD_R":0,"BODY_Y":41,"R_SHOU":74,"HEAD_P":-5,"R_ELBO":55,"L_ELBO":-57,"HEAD_Y":6,"L_SHOU":-70}
"""

W0_poses=[
    {"HEAD_R":0,"BODY_Y":52,"R_SHOU":79,"HEAD_P":-1,"R_ELBO":64,"L_ELBO":-70,"HEAD_Y":0,"L_SHOU":-69},
    {"HEAD_R":0,"BODY_Y":52,"R_SHOU":99,"HEAD_P":1,"R_ELBO":-1,"L_ELBO":3,"HEAD_Y":0,"L_SHOU":-94},
    {"HEAD_R":0,"BODY_Y":52,"R_SHOU":-15,"HEAD_P":1,"R_ELBO":39,"L_ELBO":-60,"HEAD_Y":0,"L_SHOU":-81}
]

W1_poses=[
    {"HEAD_R":0,"BODY_Y":-25,"R_SHOU":-31,"HEAD_P":-21,"R_ELBO":12,"L_ELBO":-15,"HEAD_Y":-22,"L_SHOU":-81},
    {"HEAD_R":0,"BODY_Y":-12,"R_SHOU":-46,"HEAD_P":-13,"R_ELBO":-3,"L_ELBO":-8,"HEAD_Y":21,"L_SHOU":-81},
    {"HEAD_R":0,"BODY_Y":-27,"R_SHOU":-19,"HEAD_P":-14,"R_ELBO":73,"L_ELBO":-49,"HEAD_Y":-23,"L_SHOU":-81}
]

W2_poses=[
    {"HEAD_R":0,"BODY_Y":0,"R_SHOU":45,"HEAD_P":-23,"R_ELBO":94,"L_ELBO":-93,"HEAD_Y":-22,"L_SHOU":-45},
    {"HEAD_R":0,"BODY_Y":1,"R_SHOU":45,"HEAD_P":-16,"R_ELBO":94,"L_ELBO":-93,"HEAD_Y":32,"L_SHOU":-45},
    {"HEAD_R":0,"BODY_Y":0,"R_SHOU":-32,"HEAD_P":-21,"R_ELBO":2,"L_ELBO":-57,"HEAD_Y":-24,"L_SHOU":-77}
]

W3_poses=[
    {"HEAD_R":0,"BODY_Y":0,"R_SHOU":-29,"HEAD_P":-22,"R_ELBO":0,"L_ELBO":0,"HEAD_Y":-24,"L_SHOU":-88},
    {"HEAD_R":0,"BODY_Y":37,"R_SHOU":-29,"HEAD_P":-8,"R_ELBO":0,"L_ELBO":-37,"HEAD_Y":14,"L_SHOU":-78},
    {"HEAD_R":0,"BODY_Y":-9,"R_SHOU":-6,"HEAD_P":-20,"R_ELBO":81,"L_ELBO":-53,"HEAD_Y":-16,"L_SHOU":-78}
]

W4_poses=[
    {"HEAD_R":0,"BODY_Y":42,"R_SHOU":81,"HEAD_P":-5,"R_ELBO":35,"L_ELBO":-39,"HEAD_Y":-2,"L_SHOU":-82},
    {"HEAD_R":0,"BODY_Y":41,"R_SHOU":96,"HEAD_P":11,"R_ELBO":17,"L_ELBO":-22,"HEAD_Y":-2,"L_SHOU":-89},
    {"HEAD_R":0,"BODY_Y":52,"R_SHOU":98,"HEAD_P":-9,"R_ELBO":27,"L_ELBO":-6,"HEAD_Y":-19,"L_SHOU":28}
]


W0_lines=[
    "こんにちは",
    "今日は実験に参加して頂きありがとうございます",
    "今から3つの商品のレビューを3つずつ説明します"
]

W1_lines=[
    "とてもストレスフリーです。",
    "全然役に立ってません笑猫５匹の家庭にはムリでした。猫の砂なんか全然吸わないし、猫毛も人間の髪もゴミもあまり吸わない。",
    "もう少し音が静かだったり、パーツがいくつかあるので収納方法があればより良いとは思いますが、ひっくるめてこの商品に出会えて大大大満足です！"
]

W2_lines=[
    "安さゆえ、本体は少々大きいですし、ホース先についているヘッドは、軽いプラスチックで作られているため、質が劣って見えたりもしますが、吸い込む馬力（レベル）は自分で調整が出来ますので、非常に便利です！ ",
    "ついたホコリも、水で洗い流しておけるので、お手入れもラクチン。",
    "それ以降はスムーズに外れますので、固いのは最初だけです。"
]

W3_lines=[
    "色もキレイなので部屋の片隅あってもいい感じです。",
    "プラスチックの先端部分の返しに、ゴミがはまり込む構造も難点です。",
    "とても軽くて、吸引力もあり大変満足しています。"
]

W4_lines=[
    "これで実験は終わりです",
    "今日は実験に参加して頂きありがとうございました",
    "実験者の指示に従い、アンケートへの回答をお願いします"
]


W0 = [
    {"lines":W0_lines[0],
        "poses":W0_poses[0]},
    {"lines":W0_lines[1],
        "poses":W0_poses[1]},
    {"lines":W0_lines[2],
        "poses":W0_poses[2]}
]

W1 = [
    {"lines":W1_lines[0],
        "poses":W1_poses[0]},
    {"lines":W1_lines[1],
        "poses":W1_poses[1]},
    {"lines":W1_lines[2],
        "poses":W1_poses[2]}
]

W2 = [
    {"lines":W2_lines[0],
        "poses":W2_poses[0]},
    {"lines":W2_lines[1],
        "poses":W2_poses[1]},
    {"lines":W2_lines[2],
        "poses":W2_poses[2]}
]

W3 = [
    {"lines":W3_lines[0],
        "poses":W3_poses[0]},
    {"lines":W3_lines[1],
        "poses":W3_poses[1]},
    {"lines":W3_lines[2],
        "poses":W3_poses[2]}
]

W4 = [
    {"lines":W4_lines[0],
        "poses":W4_poses[0]},
    {"lines":W4_lines[1],
        "poses":W4_poses[1]},
    {"lines":W4_lines[2],
        "poses":W4_poses[2]}
]