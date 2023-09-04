#Corn Yeald Estimates

print("This program will give you a yeild estimate a acre of for corn")


#total number of harvastable ears in 1/1000 of an acre
num_harvastable_ears = float(input("Total number of harvastable ears per 1/1000 of an acre: "))

#the number of rows on each ear
ear_1_num_rows = float(input("Number of rows on ear 1: "))

#number of kernals in each row
ear_1_krow_a = float(input("Number of kernals in ear 1 row 1: "))
ear_1_krow_b = float(input("Number of kernals in ear 1 row 2: "))
ear_1_krow_c = float(input("Number of kernals in ear 1 row 3: "))

#the number of rows on each ear
ear_2_num_rows = float(input("Number of rows on ear 2: "))
#number of kernals in each row
ear_2_krow_a = float(input("Number of kernals in ear 2 row 1: "))
ear_2_krow_b = float(input("Number of kernals in ear 2 row 2: "))
ear_2_krow_c = float(input("Number of kernals in ear 2 row 3: "))

#the number of rows on each ear
ear_3_num_rows = float(input("Number of rows on ear 3: "))
#number of kernals in each row
ear_3_krow_a = float(input("Number of kernals in ear 3 row 1: "))
ear_3_krow_b = float(input("Number of kernals in ear 3 row 2: "))
ear_3_krow_c = float(input("Number of kernals in ear 3 row 3: "))

#the number of rows on each ear
ear_4_num_rows = float(input("Number of rows on ear 4: "))
#number of kernals in each row
ear_4_krow_a = float(input("Number of kernals in ear 4 row 1: "))
ear_4_krow_b = float(input("Number of kernals in ear 4 row 2: "))
ear_4_krow_c = float(input("Number of kernals in ear 4 row 3: "))

#the number of rows on each ear
ear_5_num_rows = float(input("Number of rows on ear 5: "))
#number of kernals in each row
ear_5_krow_a = float(input("Number of kernals in ear 5 row 1: "))
ear_5_krow_b = float(input("Number of kernals in ear 5 row 2: "))
ear_5_krow_c = float(input("Number of kernals in ear 5 row 3: "))

#the number of rows on each ear
ear_6_num_rows = float(input("Number of rows on ear 6: "))
#number of kernals in each row
ear_6_krow_a = float(input("Number of kernals in ear 6 row 1: "))
ear_6_krow_b = float(input("Number of kernals in ear 6 row 2: "))
ear_6_krow_c = float(input("Number of kernals in ear 6 row 3: "))


#avarage number of kernals per row on each ear
av_num_ker_per_row_1 = (ear_1_krow_a + ear_1_krow_b + ear_1_krow_c)/3
av_num_ker_per_row_2 = (ear_2_krow_a + ear_2_krow_b + ear_2_krow_c)/3
av_num_ker_per_row_3 = (ear_3_krow_a + ear_3_krow_b + ear_3_krow_c)/3
av_num_ker_per_row_4 = (ear_4_krow_a + ear_4_krow_b + ear_4_krow_c)/3
av_num_ker_per_row_5 = (ear_5_krow_a + ear_5_krow_b + ear_5_krow_c)/3
av_num_ker_per_row_6 = (ear_6_krow_a + ear_6_krow_b + ear_6_krow_c)/3


#total number of kernals per ear (kernals per row * num of rows)
ker_per_ear_1 = av_num_ker_per_row_1 * ear_1_num_rows
ker_per_ear_2 = av_num_ker_per_row_2 * ear_2_num_rows
ker_per_ear_3 = av_num_ker_per_row_3 * ear_3_num_rows
ker_per_ear_4 = av_num_ker_per_row_4 * ear_4_num_rows
ker_per_ear_5 = av_num_ker_per_row_5 * ear_5_num_rows
ker_per_ear_6 = av_num_ker_per_row_6 * ear_6_num_rows


#avarage number of kernals per ear (sum of all kernals per ear)
av_num_ker_per_ear = (ker_per_ear_1 + ker_per_ear_2 + ker_per_ear_3 + ker_per_ear_4 + ker_per_ear_5 + ker_per_ear_6)/6



#estimated yeild for good year
est_yeild_good = (av_num_ker_per_ear * num_harvastable_ears) / 80
print("Estimated yield for a good year:", round(est_yeild_good,1))

#estimated yeild for average year
est_yeild_average = (av_num_ker_per_ear * num_harvastable_ears) / 90
print("Estimated yield for a average year:", round(est_yeild_average,1))

#estimated yeild for poor year
est_yeild_poor = (av_num_ker_per_ear * num_harvastable_ears) / 100
print("Estimated yield for a poor year:", round(est_yeild_poor,1))






