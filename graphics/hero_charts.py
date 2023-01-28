import multiprocessing as mp

import matplotlib.pyplot as plt
from matplotlib import ticker

from constants import pretty
from model.hero_model import HeroComposite

logger = mp.get_logger()


class HeroArtist:

    @classmethod
    def display_hero_attr_comparison(cls, hero_list: list[HeroComposite]):
        logger.debug('display_hero_attr_comparison')
        display_values: dict[str: dict[str: list[int or float]]] = {}
        # attr_names = ['hp', 'dodge', 'spd', 'dmg', 'crit']
        attr_names = ['hp', 'dodge', 'spd', 'lower_dmg', 'upper_dmg', 'crit']
        for name in attr_names:
            display_values[name] = {}

        for hero in hero_list:
            logger.debug(hero)
            hero_name = hero.get_name().value

            display_values['hp'][hero_name] = []
            display_values['dodge'][hero_name] = []
            display_values['spd'][hero_name] = []
            display_values['lower_dmg'][hero_name] = []
            display_values['upper_dmg'][hero_name] = []
            display_values['crit'][hero_name] = []

            for stats in hero.get_stats():
                display_values['hp'][hero_name].append(stats.get_hp().value)
                display_values['dodge'][hero_name].append(stats.get_dodge().value)
                display_values['spd'][hero_name].append(stats.get_spd().value)
                display_values['lower_dmg'][hero_name].append(stats.get_dmg().lower)
                display_values['upper_dmg'][hero_name].append(stats.get_dmg().upper)
                display_values['crit'][hero_name].append(stats.get_crit().value)

        logger.debug(pretty(display_values))

        for attr_name, hero_attrs_dict in display_values.items():
            logger.debug(f'{attr_name}: {hero_attrs_dict}')
            equal_values_indexes: list[list[tuple[int, int]]] = []
            all_values_indexes: list[int] = []
            hero_names_list: list[str] = list(hero_attrs_dict.keys())
            logger.debug(f'{hero_names_list}')
            hero_values_list: list[list[int]] = list(hero_attrs_dict.values())
            logger.debug(f'{hero_values_list}')
            for i in range(len(hero_values_list)):
                logger.debug(f'{i}')
                if i in all_values_indexes:
                    continue
                values: list[tuple[int, int]] = []
                for j in range(len(hero_values_list)):
                    logger.debug(f'{j}')
                    if i == j:
                        continue
                    if all(x == y for x, y in zip(hero_values_list[i], hero_values_list[j])):
                        logger.debug(f'{i} {j}')
                        values.append((i, j))
                        if i not in all_values_indexes:
                            all_values_indexes.append(i)
                        all_values_indexes.append(j)
                if len(values) > 0:
                    equal_values_indexes.append(values)

            for index_list in equal_values_indexes:
                second_indexes = []
                # logger.debug(f'')
                first_index, _ = index_list[0]
                for _, second_index in index_list:
                    second_indexes.append(second_index)
                # logger.debug(f'')
                names = [hero_names_list[first_index]]
                names.extend(hero_names_list[i] for i in second_indexes)
                accumulator_key = ' '.join(names)
                # logger.debug(f'')
                hero_attrs_dict[accumulator_key] = hero_values_list[first_index]
                for name in names:
                    del hero_attrs_dict[name]

        x_values = [n for n in range(1, 6)]
        for i, tup in enumerate(display_values.items()):
            attr_name, hero_attrs_dict = tup[0], tup[1]
            # for attr_name, hero_attrs_dict in display_values.items():
            fig, ax_dict = plt.subplot_mosaic([['graphic_axes'], ['legend_axes']], layout='constrained')
            # fig = plt.figure(i, layout='constrained')
            # graphic_axes = fig.add_subplot(111)
            graphic_axes = ax_dict['graphic_axes']
            graphic_axes.set_title(f"Heroes {attr_name} comparison by level")
            graphic_axes.set_xlabel('Resolve level')  # Add an x-label to the axes.
            graphic_axes.set_ylabel(f'{attr_name}')  # Add a y-label to the axes.
            graphic_axes.xaxis.set_major_locator(ticker.MultipleLocator(1))

            for hero_name, values in hero_attrs_dict.items():
                y_values = [v for v in values]
                names = hero_name.split(' ')
                hero_name = '_'.join(name[:4] for name in names)
                graphic_axes.plot(x_values, y_values, label=hero_name)

            handles, labels = graphic_axes.get_legend_handles_labels()
            legend_axes = ax_dict['legend_axes']
            legend_axes.axis('off')
            legend_axes.legend(handles, labels, loc='upper left', ncol=2)
            # graphic_axes.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0.)

            # text = ax.text(-0.2, 1.05, "Aribitrary text", transform=ax.transAxes)
            graphic_axes.grid('on')
            # fig.savefig(f'{i:03}.png', bbox_extra_artists=(lgd, text), bbox_inches='tight')
            fig.savefig(f'{i:03}.png')

            #
            #
            # fig, ax = plt.subplots()
            # ax.set_title(f"Heroes {attr_name} comparison by level")  # Add a title to the axes.
            # ax.set_xlabel('Resolve level')  # Add an x-label to the axes.
            # ax.set_ylabel(f'{attr_name}')  # Add a y-label to the axes.
            # logger.debug(hero_attrs_dict)
            # for hero_name, values in hero_attrs_dict.items():
            #     y_values = [v for v in values]
            #     logger.debug(y_values)
            #     ax.plot(x_values, y_values, label=hero_name)  # Plot some data on the axes.
            # # ax.legend()  # Add a legend.
            #
            # # Shrink current axis's height by 10% on the bottom
            # # box = ax.get_position()
            # # ax.set_position([box.x0, box.y0 + box.height * 0.2,
            # #                  box.width, box.height * 0.8])
            #
            # # Put a legend below current axis
            # # ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
            # #           fancybox=True, shadow=True, ncol=5)
            # fig.legend(loc=7)
            # fig.tight_layout()
            #
            # fig.savefig(f'{i:03}.png')
            # i += 1
            # # time.sleep(1000)
