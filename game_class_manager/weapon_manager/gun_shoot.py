from config import FLAME_DISPLAY_TIME
from game_class.prop import Clip
from game_class_manager.weapon_manager.etc import make_shell
from game_work import game_manager


def play_gun_sound(weapon, gun):
    match gun:
        # pistol
        case 'M1911':
            weapon.m1911_shoot.play()
        case 'M92':
            weapon.m92_shoot.play()
        case 'DEGLE':
            weapon.degle_shoot.play()
        case 'M500':
            weapon.m500_shoot.play()
        case 'QHAND':
            weapon.qhand_shoot.play()
        # smg
        case 'AKS74':
            weapon.aks74_shoot.play()
        case 'UMP':
            weapon.ump_shoot.play()
        case 'VECTOR':
            weapon.vector_shoot.play()
        case 'THOMPSON':
            weapon.thompson_shoot.play()
        case 'P90':
            weapon.p90_shoot.play()
        # ar
        case 'SCAR_H':
            weapon.scar_shoot.play()
        case 'M16':
            weapon.m16_shoot.play()
        case 'MP44':
            weapon.mp44_shoot.play()
        case 'AUG':
            weapon.aug_shoot.play()
        case 'GROZA':
            weapon.groza_shoot.play()
        # rifle
        case 'M1':
            weapon.m1_shoot.play()
            if weapon.cur_ammo == 1:
                weapon.m1_clip.play()
        case 'WIN':
            weapon.win_shoot.play()
        case 'MINI14':
            weapon.mini14_shoot.play()
        case 'FAL':
            weapon.fal_shoot.play()
        case 'LVOAS':
            weapon.lvoas_shoot.play()


def shoot_gun(weapon):
    if weapon.trigger and weapon.weapon_type == 0:
        if weapon.shoot_delay <= 0:  # 딜레이는 총마다 다르며, 딜레이 수치가 낮을수록 연사 속도가 빠르다. 0이 될 때마다 발사된다.
            # True일시 해당 값을 Target 클래스로 전달하여 Target 클래스의 recoil을 증가시킨다.
            if not weapon.reloading and not weapon.reload_need:  # 재장전 중이거나 재장전이 필요하면 발사되지 않는다
                weapon.shoot = True

                if weapon.gun == 'M1911':
                    weapon.shoot_delay = 65
                    weapon.p.shake_range = 15

                elif weapon.gun == 'M92':
                    weapon.shoot_delay = 55
                    weapon.p.shake_range = 15

                elif weapon.gun == 'DEGLE':
                    weapon.shoot_delay = 120
                    weapon.p.shake_range = 25

                elif weapon.gun == 'M500':
                    weapon.shoot_delay = 170
                    weapon.p.shake_range = 30
                    weapon.flame_display_time = FLAME_DISPLAY_TIME

                elif weapon.gun == 'QHAND':
                    weapon.shoot_delay = 40
                    weapon.p.shake_range = 20
                    if weapon.fire_pos == 'in':  # 쌍권총이므로 번갈아 가면서 쏘기 때문에 불꽃 위치가 매번 다르다
                        weapon.fire_pos = 'out'
                    else:
                        weapon.fire_pos = 'in'
                    weapon.flame_display_time = FLAME_DISPLAY_TIME

                elif weapon.gun == 'SCAR_H':
                    weapon.shoot_delay = 38
                    weapon.p.shake_range = 17

                elif weapon.gun == 'M16':
                    weapon.shoot_delay = 28
                    weapon.p.shake_range = 15

                elif weapon.gun == 'MP44':
                    weapon.shoot_delay = 60
                    weapon.p.shake_range = 20

                elif weapon.gun == 'AUG':
                    weapon.shoot_delay = 32
                    weapon.p.shake_range = 15

                elif weapon.gun == 'GROZA':
                    weapon.shoot_delay = 26
                    weapon.p.shake_range = 15

                elif weapon.gun == 'AKS74':
                    weapon.shoot_delay = 28
                    weapon.p.shake_range = 12

                elif weapon.gun == 'UMP':
                    weapon.shoot_delay = 35
                    weapon.p.shake_range = 13

                elif weapon.gun == 'VECTOR':
                    weapon.shoot_delay = 12
                    weapon.p.shake_range = 10

                elif weapon.gun == 'THOMPSON':
                    weapon.shoot_delay = 31
                    weapon.p.shake_range = 16

                elif weapon.gun == 'P90':
                    weapon.shoot_delay = 24
                    weapon.p.shake_range = 15

                elif weapon.gun == 'M1':  # 반자동 소총이므로 연사 딜레이를 무한대로 부여함
                    weapon.shoot_delay = 99999999999999999999999
                    weapon.p.shake_range = 35
                    if weapon.cur_ammo == 1:
                        clip = Clip(weapon.p, weapon.mp, weapon.p.x, weapon.p.y - weapon.p.cam_h, weapon.p.dir)
                        game_manager.add_object(clip, 3)
                        weapon.reload_time = 150  # M1은 구조 상 완전 재장전이 더 빠르다

                elif weapon.gun == 'WIN':
                    weapon.shoot_delay = 230
                    weapon.p.shake_range = 40
                    weapon.is_spin = True
                    weapon.flame_display_time = FLAME_DISPLAY_TIME

                elif weapon.gun == 'MINI14':
                    weapon.shoot_delay = 99999999999999999999999
                    weapon.p.shake_range = 25

                elif weapon.gun == 'FAL':
                    weapon.shoot_delay = 99999999999999999999999
                    weapon.p.shake_range = 30

                elif weapon.gun == 'LVOAS':
                    weapon.shoot_delay = 35
                    weapon.p.shake_range = 25

                elif weapon.gun == 'SPRING':
                    if weapon.zoom:  # 정조준 시에만 발사 가능
                        weapon.spring_shoot.play()
                        weapon.shoot_delay = 600
                        weapon.p.shake_range = 60
                        weapon.flame_display_time = FLAME_DISPLAY_TIME
                        weapon.pen_count = 0  # 관통 개수 초기화
                        weapon.cur_ammo -= 1  # 발사 시 총알 소모
                        if weapon.cur_ammo == 0:  # 탄창의 탄약을 모두 소모하면 재장전을 해야한다.
                            weapon.reload_need = True

                elif weapon.gun == 'KAR98':
                    if weapon.zoom:  # 정조준 시에만 발사 가능
                        weapon.kar98_shoot.play()
                        weapon.shoot_delay = 600
                        weapon.p.shake_range = 60
                        weapon.flame_display_time = FLAME_DISPLAY_TIME
                        weapon.pen_count = 0  # 관통 개수 초기화
                        weapon.cur_ammo -= 1  # 발사 시 총알 소모
                        if weapon.cur_ammo == 0:  # 탄창의 탄약을 모두 소모하면 재장전을 해야한다.
                            weapon.reload_need = True

                elif weapon.gun == 'M24':
                    if weapon.zoom:  # 정조준 시에만 발사 가능
                        weapon.m24_shoot.play()
                        weapon.shoot_delay = 700
                        weapon.p.shake_range = 70
                        weapon.flame_display_time = FLAME_DISPLAY_TIME
                        weapon.pen_count = 0  # 관통 개수 초기화
                        weapon.cur_ammo -= 1  # 발사 시 총알 소모
                        if weapon.cur_ammo == 0:  # 탄창의 탄약을 모두 소모하면 재장전을 해야한다.
                            weapon.reload_need = True

                elif weapon.gun == 'AWP':
                    if weapon.zoom:  # 정조준 시에만 발사 가능
                        weapon.awp_shoot.play()
                        weapon.shoot_delay = 700
                        weapon.p.shake_range = 70
                        weapon.flame_display_time = FLAME_DISPLAY_TIME
                        weapon.pen_count = 0  # 관통 개수 초기화
                        weapon.cur_ammo -= 1  # 발사 시 총알 소모
                        if weapon.cur_ammo == 0:  # 탄창의 탄약을 모두 소모하면 재장전을 해야한다.
                            weapon.reload_need = True

                elif weapon.gun == 'CHEYTAC':
                    if weapon.zoom:  # 정조준 시에만 발사 가능
                        weapon.cheytac_shoot.play()
                        weapon.shoot_delay = 1000
                        weapon.p.shake_range = 100
                        weapon.flame_display_time = FLAME_DISPLAY_TIME
                        weapon.pen_count = 0  # 관통 개수 초기화
                        weapon.cur_ammo -= 1  # 발사 시 총알 소모
                        if weapon.cur_ammo == 0:  # 탄창의 탄약을 모두 소모하면 재장전을 해야한다.
                            weapon.reload_need = True

                play_gun_sound(weapon, weapon.gun)

                # 일부 총기는 장전 시 탄피를 배출하므로 예외 처리
                if not weapon.gun_type == 'sr' and not weapon.gun == 'WIN' and not weapon.gun == 'M500' and\
                        not weapon.gun == 'QHAND':  # 총 종류에 따라 탄피 크기가 다르다
                    if weapon.gun_type == 'smg' or weapon.gun_type == 'pistol':
                        make_shell(weapon)

                    elif weapon.gun_type == 'ar':
                        make_shell(weapon, 18, 18)

                    elif weapon.gun_type == 'rifle':
                        if weapon.gun == 'MINI14':  # mini14는 5.56mm보통탄을 쓰므로 예외
                            make_shell(weapon, 18, 18)
                        else:
                            make_shell(weapon, 20, 20)

                    weapon.flame_display_time = FLAME_DISPLAY_TIME

                if weapon.gun == 'VECTOR':  # 연사 속도가 매우 빠르므로 총구 화염 출력시간은 더 짧게 부여
                    weapon.flame_display_time = 6

                if not weapon.gun_type == 'sr':
                    weapon.cur_ammo -= 1  # 발사 시 총알 소모
                    if weapon.cur_ammo == 0:  # 탄창의 탄약을 모두 소모하면 재장전을 해야한다.
                        weapon.reload_need = True  # 더 이상 발사되지 않는다

        else:
            weapon.shoot = False
