# ynoteios-appium-test

测试框架：appium1.6

测试项目：ynote（有道云笔记ios）

测试依赖：xcode8+、ios9.3+

项目语言：python



测试脚本中规定：
1.脚本命名为 *_test.py,方便后面统一运行
2.脚本中的测试用例方法名为 test 开头



项目结构图：

ynoteios-appium-test
     Common －－－－－－－－－－－－－－－－－－－－－－－公用集
           common.py －－－－－－－－－－－－－－－－－－公共方法，setup,等

     Constant－－－－－－－－－－－－－－－－－－－－－常量数据集：测试数据
           create_constant.py－－－－－－－－－－－－常量集：创建
           editor_constant.py－－－－－－－－－－－－常量集：编辑
           ...

     TestCase-note－－－－－－－－－－－－－－－－－－ 云笔记测试用例集
          Create－－－－－－－－－－－－－－－－－－－－用例：创建
                create_audioword_test.py－－－－－ 创建语音速记
                create_mdword_test.py－－－－－－－－创建markdown
                ...

          EditorTool－－－－－－－－－－－－－－－－－－用例：编辑器工具栏
          Share －－－－－－－－－－－－－－－－－－－－－用例：分享
          ...

     TestCase-group－－－－－－－－－－－ －－－－－－－云协作测试用例集(暂无内容)

     AllRun.py －－－－－－－－－－－－－－－－－－－－－入口，运行所有用例

     SingleRun.py －－－－－－－－－－－－－－－－－－－筛选部分用例运行

     AppiumServer.py －－－－－－－－－－－－－－－－－控制appium 服务

     caseList.txt －－－－－－－－－－－－－－－－－－－用例筛选列表

     report.html －－－－－－－－－－－－－－－－－－－－测试报告（运行时生成）

     sendEmailreport.py －－－－－－－－－－－－－－－－结果发送邮件

     README.md－－－－－－－－－－－－－－－－－－－－－－说明文案



