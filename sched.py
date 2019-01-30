from functions import *


db_path = "data/"
db_count_names = []
db_time_names = []


if os.path.isfile( db_path + 'count_names.pkl'):
    db_count_names = read_pkl(db_path + 'count_names.pkl', 'rb')

if os.path.isfile( db_path + 'time_names.pkl'):
    db_time_names = read_pkl(db_path + 'time_names.pkl', 'rb')




now = datetime.datetime.now()
date = str(now.year) + "/" + str(now.month) + "/" + str(now.day)
time = date + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

if sys.argv[1] == "create":
    activity_name = sys.argv[2]
    if sys.argv[3] == "count":
        db_count_names = db_count_names + [sys.argv[2]]
        os.mkdir(db_path + sys.argv[2])
        write_pkl(db_count_names, db_path + 'count_names.pkl', 'wb')

    elif sys.argv[3] == "time":
        db_time_names = db_time_names + [sys.argv[2]]
        os.mkdir(db_path + sys.argv[2])
        write_pkl(db_time_names, db_path + 'time_names.pkl', 'wb')

elif sys.argv[1] == "count":
    activity_name = sys.argv[2]
    count = float(sys.argv[3])
    if activity_name in db_count_names:
        # if os.path.isfile( db_path + activity_name + "/" + 'time_names.pkl')


        if os.path.isfile(db_path + activity_name + "/" +  activity_name + ".pkl"):
            data = read_pkl(db_path + activity_name + "/" +  activity_name + ".pkl", 'rb')

            if data[-1][0] == date:
                data[-1][1] = float(data[-1][1]) + count
            else:
                data = np.concatenate((data,[[date, count]]))

            write_pkl(data, db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            print(data)

        else:
            data = np.array([[date, count]])
            write_pkl(data, db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            print(data)


elif sys.argv[1] == "start":
    activity_name = sys.argv[2]
    if activity_name in db_time_names:
        if os.path.isfile(db_path + activity_name + "/" +  activity_name + ".pkl"):
            data = read_pkl(db_path + activity_name + "/" +  activity_name + ".pkl", 'rb')
            data = np.concatenate((data,[[time, ""]]))
            write_pkl(data, db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            print(data)
        else:
            data = np.array([[time, ""]])
            write_pkl(data, db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            print(data)

elif sys.argv[1] == "stop":
    activity_name = sys.argv[2]
    if activity_name in db_time_names:
        if os.path.isfile(db_path + activity_name + "/" +  activity_name + ".pkl"):
            data = read_pkl(db_path + activity_name + "/" +  activity_name + ".pkl", 'rb')
            data[-1][1] = time
            write_pkl(data, db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            print(data)


elif sys.argv[1] == "report":
    activity_name = sys.argv[2]

    if activity_name == "all":
        day = pd.Timestamp(date) - pd.Timedelta('1 day') * int(sys.argv[3])
        datos = [read_pkl(db_path + activity + "/" +  activity + ".pkl", 'rb') for activity in db_time_names]
        time_per_activity = [time_spent(day, d) for d in datos]
        print(time_per_activity)
        print(db_time_names)

        # labels = 'Python', 'C++', 'Ruby', 'Java'
        # sizes = [215, 130, 245, 210]
        # colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        # explode = (0.1, 0, 0, 0)  # explode 1st slice

        # Plot
        tiempos = time_per_activity + [86400 - sum(time_per_activity)]
        labels = db_time_names + ["otros"]
        plt.pie(tiempos, labels=labels ,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()


    elif activity_name in db_count_names:
        data = read_pkl(db_path + activity_name + "/" +  activity_name + ".pkl", 'rb')
        print(data)
        data = data.transpose()
        print(data)

        xs = np.array([ pd.Timestamp(x) for x in data[0]])
        ys = data[1].astype(np.float)

        df = pd.DataFrame({'x': xs, 'y': ys})
        plt.plot( 'x', 'y', data=df, linestyle='-', marker='o')
        plt.show()
    elif activity_name in db_time_names:
        data = read_pkl(db_path + activity_name + "/" +  activity_name + ".pkl", 'rb')
        f_day = pd.Timestamp(data[0][0])
        l_day = pd.Timestamp(data[-1][0])
        t_days = (l_day.date() - f_day.date()).days + 1
        print(data)
        print(t_days)
        days = [f_day + pd.Timedelta('1 day') * i for i in range(0, t_days)]
        time_spent_days = [time_spent(d, data) for d in days]
        print (days)
        print (time_spent_days)

        xs = days
        ys = time_spent_days

        df = pd.DataFrame({'x': xs, 'y': ys})
        plt.plot( 'x', 'y', data=df, linestyle='-', marker='o')
        plt.show()




# if sys.argv[1] == "planks":
#     f = open( db_path + date, "w+")
