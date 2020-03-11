import mysql.connector


class ReportTasks:
    def __init__(self, params):
        self.params = params

    def connect(self):
        self.database = params["DB_NAME"]
        self.db = mysql.connector.connect(host=params["DB_HOST"], port=params["DB_PORT"], user=params["DB_USER"],
                                        password=params["DB_PASSWORD"], database=self.database, autocommit=False)
        self.cursor = self.db.cursor()

    def sync(self):
        q_task = """SELECT tg.name, t.title, t.description 
            FROM task.tasks t , task.task_has_tags tt, task.tags tg
            where t.id = tt.task_id
            and tt.tag_id = tg.id and t.project_id = 3"""
        self.cursor.execute(q_task)
        t_data = self.cursor.fetchall() 
        for t in t_data:
            print(t[0], t[1])
            folder  = t[0]
            name = t[1].split("#")[0].replace(" ", "")
            fo = open("text/" + folder + "/" + name + ".tex", 'w')
            fo.write(t[2])
            fo.close()

    def close(self):
        self.db.close()


if __name__ == "__main__":
    params = dict()
    params["DB_NAME"] = "task"
    params["DB_HOST"] = "15.206.122.112"
    params["DB_PORT"] = 3306
    params["DB_USER"] = "rohit"
    params["DB_PASSWORD"] = "rohit123"
    r = ReportTasks(params)
    r.connect()
    r.sync()
    r.close()
    