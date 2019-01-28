import sys
import datetime
import pickle
import os
import numpy as np


db_path = "data/"
db_count_names = []
db_time_names = []


if os.path.isfile( db_path + 'count_names.pkl'):
    file = open(db_path + 'count_names.pkl', 'rb')
    db_count_names = pickle.load(file)
    print(db_count_names)
    file.close()


if os.path.isfile( db_path + 'time_names.pkl'):
    file = open(db_path + 'time_names.pkl', 'rb')
    db_time_names = pickle.load(file)
    print(db_time_names)
    file.close()




now = datetime.datetime.now()
date = str(now.year) + "/" + str(now.month) + "/" + str(now.day)
time = date + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

if sys.argv[1] == "create":
    activity_name = sys.argv[2]
    if sys.argv[3] == "count":
        db_count_names = db_count_names + [sys.argv[2]]
        os.mkdir(db_path + sys.argv[2])
        file = open(db_path + 'count_names.pkl', 'wb')
        pickle.dump(db_count_names, file)
        file.close()

    elif sys.argv[3] == "time":
        db_time_names = db_time_names + [sys.argv[2]]
        os.mkdir(db_path + sys.argv[2])
        file = open(db_path + 'time_names.pkl', 'wb')
        pickle.dump(db_time_names, file)
        file.close()

elif sys.argv[1] == "count":
    activity_name = sys.argv[2]
    count = float(sys.argv[3])
    if activity_name in db_count_names:
        # if os.path.isfile( db_path + activity_name + "/" + 'time_names.pkl')


        if os.path.isfile(db_path + activity_name + "/" +  activity_name + ".pkl"):
            file = open(db_path + activity_name + "/" +  activity_name + ".pkl", 'rb')
            data = pickle.load(file)
            file.close()

            if data[-1][0] == date:
                data[-1][1] = float(data[-1][1]) + count
            else:
                data = np.concatenate((data,[[date, count]]))

            file = open(db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            pickle.dump(data, file)
            file.close()
            print(data)

        else:
            file = open(db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            data = np.array([[date, count]])
            pickle.dump(data, file)
            file.close()
            print(data)


elif sys.argv[1] == "start":
    activity_name = sys.argv[2]
    if activity_name in db_time_names:
        if os.path.isfile(db_path + activity_name + "/" +  activity_name + ".pkl"):
            file = open(db_path + activity_name + "/" +  activity_name + ".pkl", 'rb')
            data = pickle.load(file)
            file.close()
            data = np.concatenate((data,[[time, ""]]))
            file = open(db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            pickle.dump(data, file)
            file.close()
            print(data)
        else:
            file = open(db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            data = np.array([[time, ""]])
            pickle.dump(data, file)
            file.close()
            print(data)

elif sys.argv[1] == "stop":
    activity_name = sys.argv[2]
    if activity_name in db_time_names:
        if os.path.isfile(db_path + activity_name + "/" +  activity_name + ".pkl"):
            file = open(db_path + activity_name + "/" +  activity_name + ".pkl", 'rb')
            data = pickle.load(file)
            file.close()
            data[-1][1] = time
            file = open(db_path + activity_name + "/" +  activity_name + ".pkl", 'wb')
            pickle.dump(data, file)
            file.close()
            print(data)


# if sys.argv[1] == "planks":
#     f = open( db_path + date, "w+")
