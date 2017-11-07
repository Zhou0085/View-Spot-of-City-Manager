﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

using GaodeSpotViewHelp;
using GaodeHotelHelp;
using GaodeRestaurantHelp;

namespace View_Spot_of_City_Manager
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            GaodeHotelMaster.GenerateCsvFile("shenzhen", "20bbffbabe3034722d1f379ce1436f30", "d:\\HotelData_shenzhen.csv");
        }
    }
}
