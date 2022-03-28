# def clean_a_star(path):
#     clean_path = [path[0]]
#     prev_cord = path[0]
#     for cord in path:
#         # print('cord')
#         # print(cord)
#         # print('prev_cord')
#         # print(prev_cord)
#         # print(prev_cord[0]+1)
#         # print(cord[0])
#         if cord[0] == prev_cord[0]+1 or cord[0] == prev_cord[0]-1:
#             if cord[1] == prev_cord[1]+1 or cord[1] == prev_cord[1]-1 or cord[1] == prev_cord[1]:
#             # print('it works')
#                 clean_path.append(cord)
#                 prev_cord = cord
#         elif cord[1] == prev_cord[1]+1 or cord[1] == prev_cord[1]-1:
#             if cord[0] == prev_cord[0]+1 or cord[0] == prev_cord[0]-1 or cord[0] == prev_cord[0]:
#                 clean_path.append(cord)
#                 prev_cord = cord
#         # print('')
#     return clean_path
#     #     if cord[0]+1 == prev_cord[0] or cord[0]-1 == prev_cord[0]:
#     #         if cord[0]+1 == prev_cord[0]:
#     #             if cord[1] == prev_cord[1] or cord[1]+1 == prev_cord[1] or cord[1]-1 == prev_cord[1]:
#     #                 clean_path.append(cord)
#     #         elif cord[0]-1 == prev_cord[0]:
#     #             if cord[1] == prev_cord[1] or cord[1]-1 == prev_cord:
#     #                 clean_path.append(cord)
#     #     elif cord[1]+1 == prev_cord[1] or cord[1]-1 == prev_cord[1]:
#     #         if cord[1]+1 == prev_cord[1]:
#     #             if cord[0] == prev_cord[0] or cord[0]+1 == prev_cord[1] or cord[0]-1 == prev_cord[1]:
#     #                 clean_path.append(cord)
#     #         elif cord[1]-1 == prev_cord[0]:
#     #             if cord[0] == prev_cord[0] or cord[0]-1 == prev_cord:
#     #                 clean_path.append(cord)