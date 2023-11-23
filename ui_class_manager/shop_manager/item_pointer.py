def hover_item(self):  # 아이템 위에 커서를 올리면 표시된다
    for i in range(len(self.button_x)):
        for j in range(len(self.button_y)):
            if self.button_x[i] - 75 < self.mx < self.button_x[i] + 75 and \
                    self.button_y[j] - 50 < self.my < self.button_y[j] + 50:

                if self.select_mode == 0:
                    if self.page == 1:
                        if 0 <= i <= 4 and 0 <= j <= 3:  # 아이템에 대해서만 표시한다.
                            self.ind_sel_x = i  # 표시할 위치, 페이지, 카테고리 저장
                            self.ind_sel_y = j
                            self.sel_cat = self.select_mode
                            self.ind_sel_on = True  # 선택한 이이템이 표시된다
                        else:
                            self.ind_sel_on = False  # 선택한 이이템이 표시된다

                    elif self.page == 2:
                        if j == 0 <= i <= 4:
                            self.ind_sel_x = i
                            self.ind_sel_y = j
                            self.sel_cat = self.select_mode
                            self.ind_sel_on = True
                        else:
                            self.ind_sel_on = False

                elif self.select_mode == 1:
                    if j == 0 <= i <= 4:
                        self.ind_sel_x = i
                        self.ind_sel_y = j
                        self.sel_cat = self.select_mode
                        self.ind_sel_on = True
                    else:
                        self.ind_sel_on = False

                elif self.select_mode == 2:
                    if 0 <= i <= 4 and 0 <= j <= 3:
                        self.ind_sel_x = i
                        self.ind_sel_y = j
                        self.sel_cat = self.select_mode
                        self.ind_sel_on = True
                    else:
                        self.ind_sel_on = False
