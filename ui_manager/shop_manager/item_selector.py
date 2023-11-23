from mods import play_mode
from ui_manager.shop_manager.item_gun_manager import buy_gun_page1, equip_gun_page1, buy_gun_page2, equip_gun_page2, \
    update_gun_item
from ui_manager.shop_manager.item_melee_manager import buy_melee, equip_melee, update_melee_item


def equip_item(self):  # 우클릭 시 좌클릭한 아이템과 동일할 시 해당 아이템 장착
    for i in range(len(self.button_x)):
        for j in range(len(self.button_y)):
            if self.button_x[i] - 75 < self.mx < self.button_x[i] + 75 and \
               self.button_y[j] - 50 < self.my < self.button_y[j] + 50:

                if self.select_mode == 0:  # 총
                    if self.page == 1:  # 기본무기이므로 처음부터 사용 가능
                        if not play_mode.weapon.buy_list_gun[i][j]:  # 구입하지 않은 항목 선택 시 구입
                            buy_gun_page1(self, i, j)
                        if play_mode.weapon.buy_list_gun[i][j]:  # 구입한 항목 선택 시 장착
                            equip_gun_page1(self, i, j)

                    elif self.page == 2:
                        if not play_mode.weapon.buy_list_gun2[i][j]:
                            buy_gun_page2(self, i, j)
                        if play_mode.weapon.buy_list_gun2[i][j]:
                            equip_gun_page2(self, i, j)

                    update_gun_item(self)

                elif self.select_mode == 1:  # 근접 무기
                    if not play_mode.weapon.buy_list_melee[i][j]:
                        buy_melee(self, i, j)
                    if play_mode.weapon.buy_list_melee[i][j]:
                        equip_melee(self, i, j)

                    update_melee_item(self)



    self.click = False
