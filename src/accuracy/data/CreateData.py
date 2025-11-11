def getData(query, location, success, type, details):
    return {
        "query": query,
        "reference": {
            "location": location
        },
        "answer": {
            "success": success,
            "type": type,
            "details": details,
        }
    }

def checkJob(serviceType, price, time, location):
    return {
            "serviceType": {
                "check": True if serviceType is not None else False,
                "checkName": serviceType.upper() if serviceType is not None else None
            },
            "price": {
                "check": True if price is not None else False,
                "checkName": price  # Below, Above, Equal + price
            },
            "time": {
                "check": True if time is not None else False,
                "checkName": time  
            },
            "location": {
                "check": True if location is not None else False,
                "checkName": location
            }
        }

def checkInfo(name, others, tasks, duties, excludedTasks):
    return {
        "name": name,
        "others": others,
        "tasks": tasks,
        "duties": duties,
        "excludedTasks": excludedTasks
    }

def getDatas():
    datas = []

    # --------------------------------------------------------------

    # datas.append(getData(
    #     "Tìm công việc ở Hà Nội",
    #     "Thái Bình",
    #     True,
    #     "Job",
    #     checkJob(None, None, None, "Hà Nội")
    # ))

    # # --------------------------------------------------------------

    # datas.append(getData(
    #     "Tìm công việc lương trên 1000VND?",
    #     "Thái Bình",
    #     True,
    #     "Job",
    #     checkJob(None, "Above 1000", None, "Thái Bình")
    # ))

    # # --------------------------------------------------------------

    # datas.append(getData(
    #     "Tìm công việc dọn dẹp vệ sinh gần tôi nhất",
    #     "31 Nguyễn Xiển, Hà Đông, Hà Nội",
    #     True,
    #     "Job",
    #     checkJob("Cleaning", None, None, "31 Nguyễn Xiển, Hà Đông, Hà Nội")
    # ))

    # # --------------------------------------------------------------

    # datas.append(getData(
    #     "Tìm công việc trong khoảng thời gian 7-8 giờ sáng?",
    #     "Chí Hòa, Hưng Hà, Thái Bình",
    #     True,
    #     "Job",
    #     checkJob(None, None, "07:00 hoặc 08:00", "Chí Hòa, Hưng Hà, Thái Bình")
    # ))

    # # --------------------------------------------------------------

    # datas.append(getData(
    #     "Ứng dụng có những danh mục gì?",
    #     "Hà Nội",
    #     True,
    #     "Info",
    #     checkInfo(
    #         "Other",
    #         ["Dọn dẹp vệ sinh", "Chăm sóc sức khỏe", "Bảo trì thiết bị"],
    #         None,
    #         None,
    #         None
    #     )
    # ))

    # # --------------------------------------------------------------

    # datas.append(getData(
    #     "Danh mục Dọn dẹp vệ sinh có những dịch vụ gì?",
    #     "Hà Nội",
    #     True,
    #     "Info",
    #     checkInfo(
    #         "Other",
    #         ["Dọn dẹp Phòng khách", "Dọn dẹp Phòng bếp", "Dọn dẹp Phòng tắm", "Dọn dẹp Phòng ngủ"],
    #         None,
    #         None,
    #         None
    #     )
    # ))

    # # --------------------------------------------------------------

    # datas.append(getData(
    #     "Danh mục Chăm sóc sức khỏe có những dịch vụ gì?",
    #     "Hà Nội",
    #     True,
    #     "Info",
    #     checkInfo(
    #         "Other",
    #         ["Chăm sóc Trẻ em", "Chăm sóc Người lớn tuổi", "Chăm sóc Người khuyết tật"],
    #         None,
    #         None,
    #         None
    #     )
    # ))

    # --------------------------------------------------------------

    datas.append(getData(
        "Dọn dẹp Phòng tắm cần làm những gì?",
        "Hà Nội",
        True,
        "Info",
        checkInfo(
            "Cleaning",
            None,
            [
                "Lau sạch toilet",
                "Vệ sinh vòi sen, bồn tắm, bồn rửa mặt",
                "Lau gương & đồ đạc",
                "Sắp xếp ngăn nắp vật dụng",
                "Quét & lau sàn",
                "Đổ rác"
            ],
            None,
            None
        )
    ))

    # --------------------------------------------------------------

    datas.append(getData(
        "Chăm sóc Người lớn tuổi cần làm gì?",
        "Hà Nội",
        True,
        "Info",
        checkInfo(
            "Healthcare",
            None,
            None,
            [
                "Nhắc uống thuốc (nếu đến giờ)",
                "Chuẩn bị nước hoặc đồ ăn nhẹ phù hợp",
                "Trò chuyện, cùng đi bộ nhẹ trong nhà hoặc ngoài vườn",
                "Hỗ trợ đi lại, tránh vấp ngã"
            ],
            None
        )
    ))

    # --------------------------------------------------------------

    datas.append(getData(
        "Chăm sóc Người khuyết tật không nên làm gì?",
        "Hà Nội",
        True,
        "Info",
        checkInfo(
            "Healthcare",
            None,
            None,
            None,
            [
                "Làm thay toàn bộ mọi thứ, khiến họ mất tự tin",
                "Nói chuyện theo kiểu thương hại hoặc coi thường",
                "Để ở nơi nguy hiểm (cầu thang, ổ điện, nước nóng)"
            ]
        )
    ))

    # --------------------------------------------------------------

    datas.append(getData(
        "Chăm sóc Trẻ em nên và không nên làm gì?",
        "Hà Nội",
        True,
        "Info",
        checkInfo(
            "Healthcare",
            None,
            None,
            [
                "Giám sát trẻ ăn nhẹ/uống nước đúng giờ (nếu đến bữa thì cho ăn chính)",
                "Hướng dẫn chơi trò chơi an toàn, có tính giáo dục (vẽ, ghép hình, đọc truyện)",
                "Kiểm tra và giữ cho trẻ không chạy ra khu vực nguy hiểm",
                "Quan tâm cảm xúc: trò chuyện, khích lệ, ôm ấp khi cần"
            ],
            [
                "Để trẻ chơi một mình mà không giám sát",
                "Cho ăn đồ ngọt, cay, cứng dễ hóc",
                "Cho sử dụng điện thoại, TV quá nhiều"
            ]
        )
    ))

    # --------------------------------------------------------------

    return datas