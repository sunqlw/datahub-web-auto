RES_DATA_DICT = {
    "mysql":
        {
            "type": "mysql",
            "host": "172.17.177.22",
            "port": "3306",
            "username": "root",
            "password": "bigData@123",
            "db_name": "datahub_web_auto",
            "tables": ['student_info']
        },
    "oracle":
        {
            "type": "oracle",
            "host": "172.17.177.22",
            "port": "1521",
            "server_name": "ORCLCDB",
            "username": "c##datahub",
            "password": "datahub",
            "db_name": "C##DATAHUB"
        },
    "sqlserver":
        {
            "type": "sqlserver",
            "host": "172.17.177.22",
            "port": "1433",
            "username": "sa",
            "password": "leap@123"
        },
    "db2":
        {
            "type": "db2",
            "host": "172.17.177.22",
            "port": "55005",
            "server_name": "sample",
            "username": "db2pf2",
            "password": "Safe!2020"
        },
    "postgresql":
        {
            "type": "postgresql",
            "host": "172.17.177.22",
            "port": "5432",
            "username": "root",
            "password": "hundsun"
        },
    "hana":
        {
            "type": "hana",
            "host": "172.17.177.9",
            "port": "31013",
            "username": "SYSTEM",
            "password": "bigData123"
        },
    "tidb":
        {
            "type": "tidb",
            "host": "172.17.177.22",
            "port": "4000",
            "username": "root",
            "password": "123456"
        },
    "dm":
        {
            "type": "dm",
            "host": "172.17.172.70",
            "port": "5236",
            "username": "SYSDBA",
            "password": "111111111"
        },
    "ftp":
        {
            "type": "ftp",
            "host": "172.17.177.22",
            "port": "21",
            "username": "datahub",
            "password": "datahub"
        },
    "sftp":
        {
            "type": "sftp",
            "host": "172.17.177.22",
            "port": "22",
            "username": "datahub",
            "password": "datahub"
        },
    "s3":
        {
            "accesskey": "AKIAP4MOVNBFMWGNR4IA",
            "secretkey": "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",
            "region": "china"
        },
    "hdfs":
        {
            "core-site": "core-site.xml",
            "hdfs-site": "hdfs-site.xml",
            "username": "hdfs"
        },
    "hive":
        {
            "service_model": "普通模式",
            "host": "demo19.test.com",
            "port": "10000",
            "username": "hive"
        },
    "hive_ha":
        {
            "service_model": "HA模式",
            "zk_host": "demo19.test.com,demo20.test.com",
            "port": "2181",
            "space_name": "hiveserver2",
            "username": "hive"
        },
    "hbase":
        {
            "zk_host": "demo19.test.com,demo20.test.com,demo21.test.com",
            "port": "2181",
            "znode": "/hbase-unsecure",
            "username": "hbase"
        }
}
