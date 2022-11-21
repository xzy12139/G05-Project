## SQL部分

这里主要用来放数据库的.sql文件，方便所有成员可以对数据库进行基本的浏览



#### .sql文件导出方式：

【注意，请在管理员模式下运行】

+ 右击mysql
+ 选择”打开文件所在位置“
+ 双击文件路径，输入cmd，（或者cmd直接定位到mysql的bin文件）
+ 输入 mysqldump -u username -p dbname > name.sql； 
  + username：你的用户名，一般是root
  + dbname：要导出的数据库名称
  + name.sql：要导出的.sql名称，请包含路径，例如D:\output.sql



#### .sql文件导入方式

+ 进入mysql
+ use数据库
+ 执行 source name.sql
  + name.sql：要导出的.sql名称，请包含路径，例如D:\output.sql