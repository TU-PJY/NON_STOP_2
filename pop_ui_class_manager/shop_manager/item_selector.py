from mods import play_mode
from pop_ui_class_manager.shop_manager.item_expendable_manager import buy_expendables
from pop_ui_class_manager.shop_manager.item_gun_manager import buy_gun_page1, equip_gun_page1, buy_gun_page2, \
    equip_gun_page2, \
    update_gun_item
from pop_ui_class_manager.shop_manager.item_melee_manager import buy_melee, equip_melee, update_melee_item


def select_item(self):  # 우클릭 시 좌클릭한 아이템과 동일할 시 해당 아이템 장착
    for i in range(len(self.button_x)):
        for j in range(len(self.button_y)):
            if self.button_x[i] - 75 < self.mx < self.button_x[i] + 75 and \
                    self.button_y[j] - 50 < self.my < self.button_y[j] + 50:
                if self.select_mode == 0:  # 총
                    if self.page == 1:  # 기본무기이므로 처음부터 사용 가능
                        if 0 <= i <= 4 and 0 <= j <= 3:
                            if not play_mode.weapon.buy_list_gun[i][j]:  # 구입하지 않은 항목 선택 시 구입
                                buy_gun_page1(i, j)
                            if play_mode.weapon.buy_list_gun[i][j]:  # 구입한 항목 선택 시 장착
                                equip_gun_page1(self, i, j)

                    elif self.page == 2:
                        if j == 0 <= i <= 4:
                            if not play_mode.weapon.buy_list_gun2[i][j]:
                                buy_gun_page2(i, j)
                            if play_mode.weapon.buy_list_gun2[i][j]:
                                equip_gun_page2(self, i, j)

                    update_gun_item(self)

                elif self.select_mode == 1:  # 근접 무기
                    if j == 0 <= i <= 4:
                        if not play_mode.weapon.buy_list_melee[i][j]:
                            buy_melee(i, j)
                        if play_mode.weapon.buy_list_melee[i][j]:
                            equip_melee(self, i, j)

                    update_melee_item(self)

                elif self.select_mode == 2:  # 소모품 및 능력치
                    if 0 <= i <= 4 and 0 <= j <= 1:
                        buy_expendables(self, i, j)

    self.click = False
