COMPONENT_NAME_DICT = {
    'rds_exct': 'RDS抽取',
    'hdfs_exct': 'HDFS文件抽取',
    'ftp_exct': 'FTP文件抽取',
    'local_exct': '本地文件抽取',
    's3_exct': 'AWS S3',
    'merge': '合并',
    'str_replace': '字符替换',
    'null_replace': '空值转换',
    'str_remove': '剔除字符',
    'newline_replace': '替换换行符',
    'space_remove': '去除首尾空格',
    'substr': '字符串长度截取',
    'date_transform': '日期格式转换',
    'add_date': '增加时间戳',
    'add_constant': '增加常值',
    'table_join': '表关联',
    'csv': '分隔符文件解析',
    'excel': 'Excel解析',
    'hbase_load': 'HBase加载',
    'hive_load': 'Hive加载',
    'hdfs_load': 'HDFS加载',
    'rds_load': 'RDS加载',
}
DB_TYPE_DICT = {
    "mysql": "MySQL",
    "oracle": "Oracle",
    "sqlserver": "SQL Server",
    "db2": "DB2",
    "postgresql": "PostgreSQL",
    "hana": "HANA",
    "tidb": "TiDB",
    "dm": "达梦",
    "hive": "Hive",
    "hdfs": "HDFS",
    "hbase": "HBase",
    "ftp": "FTP",
    "s3": "AWS S3"
}
MODEL_NAME_DICT = {
    "new": "新建空白画布",
    "rds_to_hive": "RDS to Hive",
    "rds_to_hbase": "RDS to HBase",
    "rds_to_hdfs": "RDS to HDFS",
    "ftp_to_hive": "FTP to Hive",
    "ftp_to_hdfs": "FTP to HDFS",
    "local_excel_to_hive": "本地Excel to Hive",
    "local_csv_to_hive": "本地分隔符文件 to Hive",
    "hdfs_to_hive": "HDFS to Hive",
    "s3_to_hive": "AWS S3 to Hive",
    "s3_to_hdfs": "AWS S3 to HDFS",
    "cdc_to_hive": "CDC to Hive"
}
MESSAGE_DICT = {
    "save_success": "保存成功",
    "run_success": "启动成功",
    "res_name_exist": "Resource name is already exist."
}
