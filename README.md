# A URDF Dataset

This repository contains a dataset of URDF Collections from various sources.
All the URDF Collections can be found in the subdirectory _urdf\_files_.
We have manually constructed a duplicates directory containing the robots with duplicate URDF Collections from different sources. This can be found in the _duplicates_ subdirectory.
Scripts for producing analysis results on the dataset, can be found in the _scripts_ subdirectory.

## Robots
<table>
<thead>
<tr><th>name</th><th>variant</th><th>id</th><th>sources</th><th>type</th></tr>
</thead>
<tbody>
<tr><td>2F-140 gripper</td><td>none</td><td>0</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/robotiq/robotiq_2f_140_gripper_visualization/urdf/robotiq_arg2f_140_model.urdf">ros-industrial</a>']</td><td>end effector</td></tr>
<tr><td>2F-85 gripper</td><td>none</td><td>1</td><td>['<a href="urdf_files/matlab/robotiq2F85/urdf/robotiq2F85.urdf">matlab</a>', '<a href="urdf_files/random/robot-assets/robotiq_gripper/robotiq_arg85_description.URDF">random</a>', '<a href="urdf_files/ros-industrial/xacro_generated/robotiq/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.urdf">ros-industrial</a>']</td><td>end effector</td></tr>
<tr><td>2FG7 gripper</td><td>none</td><td>2</td><td>['<a href="urdf_files/random/xacro_generated/juandpenan/onrobot_2fg7_description/urdf/onrobot_2fg7_upload.urdf">random</a>']</td><td>end effector</td></tr>
<tr><td>3F gripper</td><td>none</td><td>3</td><td>['<a href="urdf_files/drake/atlas/urdf/robotiq.urdf">drake</a>', '<a href="urdf_files/ros-industrial/robotiq/robotiq_3f_gripper_visualization/cfg/robotiq-3f-gripper_mesh.urdf">ros-industrial</a>']</td><td>end effector</td></tr>
<tr><td>AL5D</td><td>none</td><td>4</td><td>['<a href="urdf_files/robotics-toolbox/al5d_description/urdf/al5d_robot.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>ANYmal</td><td>none</td><td>5</td><td>['<a href="urdf_files/oems/anymal_anybotics/anymal_b_simple_description/urdf/anymal.urdf">oems</a>', '<a href="urdf_files/random/robot-assets/anymal/anymal.urdf">random</a>']</td><td>quadrupedal robot</td></tr>
<tr><td>Allegro hand - left</td><td>none</td><td>6</td><td>['<a href="urdf_files/drake/allegro_hand_description/urdf/allegro_hand_description_left.urdf">drake</a>']</td><td>end effector</td></tr>
<tr><td>Allegro hand - right</td><td>none</td><td>7</td><td>['<a href="urdf_files/drake/allegro_hand_description/urdf/allegro_hand_description_right.urdf">drake</a>']</td><td>end effector</td></tr>
<tr><td>Atlas</td><td>none</td><td>8</td><td>['<a href="urdf_files/matlab/Atlas/urdf/atlas.urdf">matlab</a>']</td><td>humanoid robot</td></tr>
<tr><td>BarrettHand</td><td>none</td><td>9</td><td>['<a href="urdf_files/random/robot-assets/barret_hand/bhand_model.URDF">random</a>']</td><td>end effector</td></tr>
<tr><td>Baxter</td><td>none</td><td>10</td><td>['<a href="urdf_files/matlab/baxter_description/urdf/rethinkBaxter.urdf">matlab</a>', '<a href="urdf_files/oems/baxter_rethink_robotics/baxter_description/urdf/baxter.urdf">oems</a>']</td><td>dual arm robot</td></tr>
<tr><td>C2 gripper</td><td>none</td><td>11</td><td>['<a href="urdf_files/ros-industrial/robotiq/robotiq_2f_c2_gripper_visualization/urdf/robotiq_c2_model.urdf">ros-industrial</a>', '<a href="urdf_files/ros-industrial/xacro_generated/robotiq/robotiq_2f_c2_gripper_visualization/urdf/robotiq_c2_model.urdf">ros-industrial</a>']</td><td>end effector</td></tr>
<tr><td>CR35iA</td><td>none</td><td>12</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_cr35ia_support/urdf/cr35ia.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>CR7iA</td><td>none</td><td>13</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_cr7ia_support/urdf/cr7ia.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>CR7iAL</td><td>none</td><td>14</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_cr7ia_support/urdf/cr7ial.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>CRB 15000</td><td>none</td><td>15</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_crb15000_support/urdf/crb15000_5_95.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>CRx10iA</td><td>none</td><td>16</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_crx10ia_support/urdf/crx10ial.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Dual Franka Panda</td><td>none</td><td>17</td><td>['<a href="urdf_files/oems/xacro_generated/franka_emika/franka_description/robots/dual_panda/dual_panda.urdf">oems</a>']</td><td>dual arm robot</td></tr>
<tr><td>EVEr3</td><td>none</td><td>18</td><td>['<a href="urdf_files/oems/eveR3_halodi/eve_r3_description/urdf/eve_r3.urdf">oems</a>', '<a href="urdf_files/random/robot-assets/halodi/eve_r3.urdf">random</a>']</td><td>humanoid robot</td></tr>
<tr><td>FR3</td><td>none</td><td>19</td><td>['<a href="urdf_files/oems/xacro_generated/franka_emika/franka_description/robots/fr3/fr3.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>FT sensor</td><td>none</td><td>20</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/robotiq/robotiq_ft_sensor/urdf/example_use_robotiq_ft300.urdf">ros-industrial</a>']</td><td>end effector</td></tr>
<tr><td>Fetch</td><td>none</td><td>21</td><td>['<a href="urdf_files/random/robot-assets/fetch/robots/fetch.urdf">random</a>', '<a href="urdf_files/robotics-toolbox/fetch_description/robots/fetch.urdf">robotics-toolbox</a>']</td><td>mobile manipulator</td></tr>
<tr><td>Franka Panda</td><td>none</td><td>22</td><td>['<a href="urdf_files/matlab/franka_description/robots/frankaEmikaPanda.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/franka_emika/franka_description/robots/panda/panda.urdf">oems</a>', '<a href="urdf_files/random/robot-assets/franka_panda/panda.urdf">random</a>', '<a href="urdf_files/robotics-toolbox/xacro_generated/franka_description/robots/panda.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>Freight</td><td>none</td><td>23</td><td>['<a href="urdf_files/robotics-toolbox/fetch_description/robots/freight.urdf">robotics-toolbox</a>']</td><td>mobile robot</td></tr>
<tr><td>Ginger</td><td>none</td><td>24</td><td>['<a href="urdf_files/random/robot-assets/ginger_robot/gingerurdf.urdf">random</a>']</td><td>humanoid robot</td></tr>
<tr><td>Husky</td><td>none</td><td>25</td><td>['<a href="urdf_files/matlab/husky_description/urdf/clearpathHusky.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>IRB 120 3 58</td><td>none</td><td>26</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb120_support/urdf/irb120_3_58.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 1200 5 90</td><td>none</td><td>27</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb1200_support/urdf/irb1200_5_90.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 1200 7 70</td><td>none</td><td>28</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb1200_support/urdf/irb1200_7_70.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 120T 3 58</td><td>none</td><td>29</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb120_support/urdf/irb120t_3_58.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 1600 6 12</td><td>none</td><td>30</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb1600_support/urdf/irb1600_6_12.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 1600 8 145</td><td>none</td><td>31</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb1600_support/urdf/irb1600_8_145.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 2600</td><td>none</td><td>32</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb2600_support/urdf/irb2600_12_165.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 4400</td><td>none</td><td>33</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb4400_support/urdf/irb4400l_30_243.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 4600 20 250</td><td>none</td><td>34</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb4600_support/urdf/irb4600_20_250.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 4600 40 255</td><td>none</td><td>35</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb4600_support/urdf/irb4600_40_255.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 4600 60 205</td><td>none</td><td>36</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb4600_support/urdf/irb4600_60_205.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 52 7 120</td><td>none</td><td>37</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb52_support/urdf/irb52_7_120.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 52 7 145</td><td>none</td><td>38</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb52_support/urdf/irb52_7_145.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 6600 60 205</td><td>none</td><td>39</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb6600_support/urdf/irb6600_225_255.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 6650s 125 350</td><td>none</td><td>40</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb6650s_support/urdf/irb6650s_125_350.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 6650s 90 390</td><td>none</td><td>41</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb6650s_support/urdf/irb6650s_90_390.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 6700 200 260</td><td>none</td><td>42</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb6700_support/urdf/irb6700_200_260.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 6700 235 265</td><td>none</td><td>43</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb6700_support/urdf/irb6700_235_265.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB 7600</td><td>none</td><td>44</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/abb/abb_irb7600_support/urdf/irb7600_150_350.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB120</td><td>none</td><td>45</td><td>['<a href="urdf_files/matlab/abb_irb120_support/urdf/abbIrb120.urdf">matlab</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB120T</td><td>none</td><td>46</td><td>['<a href="urdf_files/matlab/abb_irb120_support/urdf/abbIrb120T.urdf">matlab</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB140</td><td>none</td><td>47</td><td>['<a href="urdf_files/robotics-toolbox/abb_irb140/urdf/irb140.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB140QT</td><td>none</td><td>48</td><td>['<a href="urdf_files/robotics-toolbox/abb_irb140/urdf/irb140QT.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB1600</td><td>none</td><td>49</td><td>['<a href="urdf_files/matlab/abb_irb1600_support/urdf/abbIrb1600.urdf">matlab</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB2400</td><td>none</td><td>50</td><td>['<a href="urdf_files/ros-industrial/abb/abb_irb2400_support/urdf/irb2400.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB5400</td><td>none</td><td>51</td><td>['<a href="urdf_files/ros-industrial/abb/abb_irb5400_support/urdf/irb5400.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB6640</td><td>none</td><td>52</td><td>['<a href="urdf_files/ros-industrial/abb/abb_irb6600_support/urdf/irb6640.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Jackal</td><td>none</td><td>53</td><td>['<a href="urdf_files/matlab/jackal_description/urdf/clearpathJackal.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/jackal_clearpath_robotics/jackal_description/urdf/jackal.urdf">oems</a>']</td><td>mobile robot</td></tr>
<tr><td>Jaco J2N4S300</td><td>none</td><td>54</td><td>['<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/j2n4s300_standalone.urdf">oems</a>', '<a href="urdf_files/robotics-toolbox/xacro_generated/kinova_description/urdf/j2n4s300.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>Jaco J2N6S200</td><td>none</td><td>55</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaJacoJ2N6S200.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/j2n6s200_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Jaco J2N6S300</td><td>none</td><td>56</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaJacoJ2N6S300.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/j2n6s300_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Jaco J2N7S300</td><td>none</td><td>57</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaJacoJ2N7S300.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/j2n7s300_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Jaco J2S6S200</td><td>none</td><td>58</td><td>['<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/j2s6s200_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Jaco J2S6S300</td><td>none</td><td>59</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaJacoJ2S6S300.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/j2s6s300_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Jaco J2S7S300</td><td>none</td><td>60</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaJacoJ2S7S300.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/j2s7s300_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Jaco Two Arm</td><td>none</td><td>61</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaJacoTwoArmExample.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/two_arm_robot_example_standalone.urdf">oems</a>']</td><td>dual arm robot</td></tr>
<tr><td>Kinova Gen3</td><td>none</td><td>62</td><td>['<a href="urdf_files/matlab/kortex_description/urdf/kinovaGen3.urdf">matlab</a>', '<a href="urdf_files/robotics-toolbox/xacro_generated/kinova_description/urdf/kinovaGen3.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>Kinova Gen3 V12</td><td>none</td><td>63</td><td>['<a href="urdf_files/matlab/kortex_v12_description/robots/kinovaGen3V12.urdf">matlab</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr 120 R2500 Pro</td><td>none</td><td>64</td><td>['<a href="urdf_files/ros-industrial/kuka/kuka_kr120_support/urdf/kr120r2500pro.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr 16-2</td><td>none</td><td>65</td><td>['<a href="urdf_files/ros-industrial/kuka/kuka_kr16_support/urdf/kr16_2.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr 210 L150</td><td>none</td><td>66</td><td>['<a href="urdf_files/ros-industrial/kuka/kuka_kr210_support/urdf/kr210l150.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr10 R1100 sixx</td><td>none</td><td>67</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr10_support/urdf/kr10r1100sixx.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr10 R1420</td><td>none</td><td>68</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr10_support/urdf/kr10r1420.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr10 R900-2</td><td>none</td><td>69</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr10_support/urdf/kr10r900_2.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr150 R3100-2</td><td>none</td><td>70</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr150_support/urdf/kr150r3100_2.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr150-2</td><td>none</td><td>71</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr150_support/urdf/kr150_2.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr3 R540</td><td>none</td><td>72</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr3_support/urdf/kr3r540.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr5 ARC</td><td>none</td><td>73</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr5_support/urdf/kr5_arc.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr6 R700 sixx</td><td>none</td><td>74</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr6_support/urdf/kr6r700sixx.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr6 R900 sixx</td><td>none</td><td>75</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr6_support/urdf/kr6r900sixx.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka kr6 R900-2</td><td>none</td><td>76</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr6_support/urdf/kr6r900_2.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka lbr iiwa 14</td><td>none</td><td>77</td><td>['<a href="urdf_files/matlab/iiwa_description/urdf/kukaIiwa14.urdf">matlab</a>', '<a href="urdf_files/robotics-toolbox/kuka_description/kuka_lbr_iiwa/urdf/lbr_iiwa_14_r820.urdf">robotics-toolbox</a>', '<a href="urdf_files/ros-industrial/kuka/kuka_lbr_iiwa_support/urdf/lbr_iiwa_14_r820.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka lbr iiwa 7</td><td>none</td><td>78</td><td>['<a href="urdf_files/matlab/iiwa_description/urdf/kukaIiwa7.urdf">matlab</a>', '<a href="urdf_files/random/robot-assets/kuka_iiwa/model.urdf">random</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200i</td><td>none</td><td>79</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200i_support/urdf/lrmate200i.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iB</td><td>none</td><td>80</td><td>['<a href="urdf_files/matlab/fanuc_lrmate200ib_support/urdf/fanucLRMate200ib.urdf">matlab</a>', '<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200ib_support/urdf/lrmate200ib.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iB/3L</td><td>none</td><td>81</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200ib_support/urdf/lrmate200ib3l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iC</td><td>none</td><td>82</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200ic_support/urdf/lrmate200ic.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iC/5F</td><td>none</td><td>83</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200ic_support/urdf/lrmate200ic5f.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iC/5H</td><td>none</td><td>84</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200ic_support/urdf/lrmate200ic5h.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iC/5HS</td><td>none</td><td>85</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200ic_support/urdf/lrmate200ic5hs.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iC/5L</td><td>none</td><td>86</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200ic_support/urdf/lrmate200ic5l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iD</td><td>none</td><td>87</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200id_support/urdf/lrmate200id.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iD/4S</td><td>none</td><td>88</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200id_support/urdf/lrmate200id4s.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iD/4SC</td><td>none</td><td>89</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200id_support/urdf/lrmate200id4sc.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iD/4SH</td><td>none</td><td>90</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200id_support/urdf/lrmate200id4sh.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iD/7H</td><td>none</td><td>91</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200id_support/urdf/lrmate200id7h.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iD/7L</td><td>none</td><td>92</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200id_support/urdf/lrmate200id7l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LR Mate 200iD/7LC</td><td>none</td><td>93</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_lrmate200id_support/urdf/lrmate200id7lc.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>LWA 4D</td><td>none</td><td>94</td><td>['<a href="urdf_files/random/xacro_generated/schunk_modular_robotics/schunk_description/urdf/schunk_lwa4p.urdf">random</a>']</td><td>robotic arm</td></tr>
<tr><td>LWA 4P</td><td>none</td><td>95</td><td>['<a href="urdf_files/random/schunk_lwa4p/robot.urdf">random</a>', '<a href="urdf_files/random/xacro_generated/schunk_modular_robotics/schunk_description/urdf/schunk_lwa4d.urdf">random</a>']</td><td>robotic arm</td></tr>
<tr><td>M-10iA</td><td>none</td><td>96</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m10ia_support/urdf/m10ia.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-10iA/7L</td><td>none</td><td>97</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m10ia_support/urdf/m10ia7l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-16iB</td><td>none</td><td>98</td><td>['<a href="urdf_files/matlab/fanuc_m16ib_support/urdf/fanucM16ib.urdf">matlab</a>', '<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m16ib_support/urdf/m16ib20.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-20iA</td><td>none</td><td>99</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m20ia_support/urdf/m20ia.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-20iA/10L</td><td>none</td><td>100</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m20ia_support/urdf/m20ia10l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-20iB</td><td>none</td><td>101</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m20ib_support/urdf/m20ib25.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-430iA/2F</td><td>none</td><td>102</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m430ia_support/urdf/m430ia2f.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-430iA/2P</td><td>none</td><td>103</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m430ia_support/urdf/m430ia2p.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-6iB</td><td>none</td><td>104</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m6ib_support/urdf/m6ib.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-6iB/6S</td><td>none</td><td>105</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m6ib_support/urdf/m6ib6s.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-710iC/45M</td><td>none</td><td>106</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m710ic_support/urdf/m710ic45m.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-710iC/50</td><td>none</td><td>107</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m710ic_support/urdf/m710ic50.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-900iA260L</td><td>none</td><td>108</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m900ia_support/urdf/m900ia260l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>M-900iB700</td><td>none</td><td>109</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_m900ib_support/urdf/m900ib700.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Meca500-R3</td><td>none</td><td>110</td><td>['<a href="urdf_files/matlab/mecademic_description/urdf/meca500r3.urdf">matlab</a>']</td><td>robotic arm</td></tr>
<tr><td>MiR 100</td><td>none</td><td>111</td><td>['<a href="urdf_files/random/xacro_generated/mir_description/urdf/mir.urdf">random</a>']</td><td>mobile robot</td></tr>
<tr><td>Mico M1N4S200</td><td>none</td><td>112</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaMicoM1N4S200.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/m1n4s200_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Mico M1N6S200</td><td>none</td><td>113</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaMicoM1N6S200.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/m1n6s200_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Mico M1N6S300</td><td>none</td><td>114</td><td>['<a href="urdf_files/matlab/kinova_description/urdf/kinovaMicoM1N6S300.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/kinova_robotics/kinova_description/urdf/m1n6s300_standalone.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Motoman MH5</td><td>none</td><td>115</td><td>['<a href="urdf_files/matlab/motoman_mh5_support/urdf/yaskawaMotomanMH5.urdf">matlab</a>', '<a href="urdf_files/ros-industrial/motoman/motoman_mh5_support/urdf/mh5.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Motoman SIA10D</td><td>none</td><td>116</td><td>['<a href="urdf_files/ros-industrial/motoman/motoman_sia10d_support/urdf/sia10d.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Motoman SIA10F</td><td>none</td><td>117</td><td>['<a href="urdf_files/ros-industrial/motoman/motoman_sia10f_support/urdf/sia10f.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Motoman SIA20D</td><td>none</td><td>118</td><td>['<a href="urdf_files/ros-industrial/motoman/motoman_sia20d_support/urdf/sia20d.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Motoman SIA5D</td><td>none</td><td>119</td><td>['<a href="urdf_files/ros-industrial/motoman/motoman_sia5d_support/urdf/sia5d.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Movo</td><td>none</td><td>120</td><td>['<a href="urdf_files/matlab/movo_description/urdf/kinovaMovo.urdf">matlab</a>']</td><td>mobile manipulator</td></tr>
<tr><td>OP2</td><td>none</td><td>121</td><td>['<a href="urdf_files/matlab/robotis_op_description/robots/robotisOP2.urdf">matlab</a>']</td><td>humanoid robot</td></tr>
<tr><td>Open Manipulator</td><td>none</td><td>122</td><td>['<a href="urdf_files/matlab/open_manipulator_description/urdf/robotisOpenManipulator.urdf">matlab</a>', '<a href="urdf_files/oems/xacro_generated/open-manipulator_robotis/open_manipulator_description/urdf/open_manipulator.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>PG 70</td><td>none</td><td>123</td><td>['<a href="urdf_files/random/xacro_generated/schunk_modular_robotics/schunk_description/urdf/schunk_pg70.urdf">random</a>']</td><td>end effector</td></tr>
<tr><td>PR2</td><td>none</td><td>124</td><td>['<a href="urdf_files/drake/pr2/pr2_description/urdf/pr2_simplified.urdf">drake</a>', '<a href="urdf_files/matlab/pr2_description/robots/willowgaragePR2.urdf">matlab</a>', '<a href="urdf_files/random/robot-assets/pr2/pr2.urdf">random</a>', '<a href="urdf_files/robotics-toolbox/xacro_generated/pr2_description/robots/pr2.urdf">robotics-toolbox</a>']</td><td>mobile manipulator</td></tr>
<tr><td>PUMA 560</td><td>none</td><td>125</td><td>['<a href="urdf_files/robotics-toolbox/puma560_description/urdf/puma560_robot.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>PW 70</td><td>none</td><td>126</td><td>['<a href="urdf_files/random/xacro_generated/schunk_modular_robotics/schunk_description/urdf/schunk_pw70.urdf">random</a>']</td><td>end effector</td></tr>
<tr><td>PhantomX Pincher</td><td>none</td><td>127</td><td>['<a href="urdf_files/robotics-toolbox/pxpincher/urdf/pincher_arm.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>PincherX-100</td><td>none</td><td>128</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/px100.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>PincherX-150</td><td>none</td><td>129</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/px150.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>Pioneer 3AT</td><td>none</td><td>130</td><td>['<a href="urdf_files/matlab/amr_robots_description/urdf/amrPioneer3AT.urdf">matlab</a>', '<a href="urdf_files/oems/pioneer_adept_mobile_robots/description/urdf/pioneer3at.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Pioneer 3DX</td><td>none</td><td>131</td><td>['<a href="urdf_files/matlab/amr_robots_description/urdf/amrPioneer3DX.urdf">matlab</a>', '<a href="urdf_files/oems/pioneer_adept_mobile_robots/description/urdf/pioneer3dx.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Pioneer LX</td><td>none</td><td>132</td><td>['<a href="urdf_files/matlab/amr_robots_description/urdf/amrPioneerLX.urdf">matlab</a>', '<a href="urdf_files/oems/pioneer_adept_mobile_robots/description/urdf/pioneer-lx.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>QArm</td><td>none</td><td>133</td><td>['<a href="urdf_files/matlab/qarm_description/urdf/quanserQArm.urdf">matlab</a>', '<a href="urdf_files/oems/qarm_quanser/qarm_description/urdf/QARM.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>QBot2e</td><td>none</td><td>134</td><td>['<a href="urdf_files/matlab/quanser_description/urdf/quanserQBot2e.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>QCar</td><td>none</td><td>135</td><td>['<a href="urdf_files/matlab/quanser_description/urdf/quanserQCar.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>R-1000iA/80F</td><td>none</td><td>136</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_r1000ia_support/urdf/r1000ia80f.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>R-2000iB/210F</td><td>none</td><td>137</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_r2000ib_support/urdf/r2000ib210f.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>R-2000iC/125L</td><td>none</td><td>138</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_r2000ic_support/urdf/r2000ic125l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>R-2000iC/165F</td><td>none</td><td>139</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_r2000ic_support/urdf/r2000ic165f.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>R-2000iC/210F</td><td>none</td><td>140</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_r2000ic_support/urdf/r2000ic210f.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>R-2000iC/210L</td><td>none</td><td>141</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_r2000ic_support/urdf/r2000ic210l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>R-2000iC/270F</td><td>none</td><td>142</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/fanuc/fanuc_r2000ic_support/urdf/r2000ic270f.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>R2-D2</td><td>none</td><td>143</td><td>['<a href="urdf_files/random/robot-assets/r2_description/robots/r2b.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2b_control.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2b_dynamics.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2b_sim_upperbody_control.urdf.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2b_sim_upperbody_dynamics.urdf.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c1.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c1_control.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c1_dynamics.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c5.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c5_control.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c5_dynamics.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c6.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c6_control.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c6_dynamics.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c6_valve.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c_sim_full_control.urdf.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c_sim_full_dynamics.urdf.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c_sim_legs_control.urdf.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c_sim_legs_dynamics.urdf.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c_sim_upperbody_control.urdf.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2c_sim_upperbody_dynamics.urdf.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2_left_forearm.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/r2_description/robots/r2_left_gripper.urdf">random</a>']</td><td>humanoid robot</td></tr>
<tr><td>RG2 gripper</td><td>none</td><td>144</td><td>['<a href="urdf_files/random/xacro_generated/osaka_university_onrobot/onrobot_rg2_visualization/urdf/onrobot_rg2_model.urdf">random</a>']</td><td>end effector</td></tr>
<tr><td>RG6 gripper</td><td>none</td><td>145</td><td>['<a href="urdf_files/random/xacro_generated/osaka_university_onrobot/onrobot_rg6_visualization/urdf/onrobot_rg6_model.urdf">random</a>']</td><td>end effector</td></tr>
<tr><td>RX 160</td><td>none</td><td>146</td><td>['<a href="urdf_files/ros-industrial/staubli/staubli_rx160_support/urdf/rx160.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>RX 160L</td><td>none</td><td>147</td><td>['<a href="urdf_files/ros-industrial/staubli/staubli_rx160_support/urdf/rx160l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>ReactorX-150</td><td>none</td><td>148</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/rx150.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>ReactorX-200</td><td>none</td><td>149</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/rx200.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>Sawyer</td><td>none</td><td>150</td><td>['<a href="urdf_files/matlab/sawyer_description/urdf/rethinkSawyer.urdf">matlab</a>']</td><td>robotic arm</td></tr>
<tr><td>Spot</td><td>none</td><td>151</td><td>['<a href="urdf_files/oems/spot_boston_dynamics/spot_base_urdf/model.urdf">oems</a>', '<a href="urdf_files/random/spot_ros/spot_description/urdf/spot.urdf">random</a>']</td><td>quadrupedal robot</td></tr>
<tr><td>Spot Arm</td><td>none</td><td>152</td><td>['<a href="urdf_files/random/spot_ros/spot_description/urdf/spot_arm.urdf">random</a>']</td><td>robotic arm</td></tr>
<tr><td>TX-60</td><td>none</td><td>153</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx60_support/urdf/tx60.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX-60L</td><td>none</td><td>154</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx60_support/urdf/tx60l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX-90</td><td>none</td><td>155</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx90_support/urdf/tx90.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX-90L</td><td>none</td><td>156</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx90_support/urdf/tx90l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX-90XL</td><td>none</td><td>157</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx90_support/urdf/tx90xl.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX2-60</td><td>none</td><td>158</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx2_60_support/urdf/tx2_60.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX2-60L</td><td>none</td><td>159</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx2_60_support/urdf/tx2_60l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX2-90</td><td>none</td><td>160</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx2_90_support/urdf/tx2_90.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX2-90L</td><td>none</td><td>161</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx2_90_support/urdf/tx2_90l.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>TX2-90XL</td><td>none</td><td>162</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/staubli/staubli_tx2_90_support/urdf/tx2_90xl.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Turtlebot</td><td>none</td><td>163</td><td>['<a href="urdf_files/matlab/turtlebot_description/robots/clearpathTurtleBot2.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 - Burger</td><td>none</td><td>164</td><td>['<a href="urdf_files/matlab/turtlebot3_description/urdf/robotisTurtleBot3Burger.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 - Waffle</td><td>none</td><td>165</td><td>['<a href="urdf_files/matlab/turtlebot3_description/urdf/robotisTurtleBot3Waffle.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 - Waffle Pi</td><td>none</td><td>166</td><td>['<a href="urdf_files/matlab/turtlebot3_description/urdf/robotisTurtleBot3WafflePi.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 - Waffle Pi for Open Manipulator</td><td>none</td><td>167</td><td>['<a href="urdf_files/matlab/turtlebot3_description/urdf/robotisTurtleBot3WafflePiForOpenManipulator.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 - Waffle for Open Manipulator</td><td>none</td><td>168</td><td>['<a href="urdf_files/matlab/turtlebot3_description/urdf/robotisTurtleBot3WaffleForOpenManipulator.urdf">matlab</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 Burger</td><td>none</td><td>169</td><td>['<a href="urdf_files/oems/xacro_generated/turtlebot3_robotis/turtlebot3_description/urdf/turtlebot3_burger.urdf">oems</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 Waffle</td><td>none</td><td>170</td><td>['<a href="urdf_files/oems/xacro_generated/turtlebot3_robotis/turtlebot3_description/urdf/turtlebot3_waffle.urdf">oems</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 Waffle Pi</td><td>none</td><td>171</td><td>['<a href="urdf_files/oems/xacro_generated/turtlebot3_robotis/turtlebot3_description/urdf/turtlebot3_waffle_pi.urdf">oems</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot Arm</td><td>none</td><td>172</td><td>['<a href="urdf_files/robotics-toolbox/pxpincher/urdf/turtlebot_arm.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>UR10</td><td>none</td><td>173</td><td>['<a href="urdf_files/matlab/ur_description/urdf/universalUR10.urdf">matlab</a>', '<a href="urdf_files/random/robot-assets/ur10/ur10_robot.urdf">random</a>', '<a href="urdf_files/robotics-toolbox/xacro_generated/ur_description/urdf/ur10.urdf">robotics-toolbox</a>', '<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_description/urdf/ur10_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR10e</td><td>none</td><td>174</td><td>['<a href="urdf_files/matlab/ur_e_description/urdf/universalUR10e.urdf">matlab</a>', '<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_e_description/urdf/ur10e_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR16e</td><td>none</td><td>175</td><td>['<a href="urdf_files/matlab/ur_e_description/urdf/universalUR16e.urdf">matlab</a>']</td><td>robotic arm</td></tr>
<tr><td>UR3</td><td>none</td><td>176</td><td>['<a href="urdf_files/matlab/ur_description/urdf/universalUR3.urdf">matlab</a>', '<a href="urdf_files/robotics-toolbox/xacro_generated/ur_description/urdf/ur3.urdf">robotics-toolbox</a>', '<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_description/urdf/ur3_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR3e</td><td>none</td><td>177</td><td>['<a href="urdf_files/matlab/ur_e_description/urdf/universalUR3e.urdf">matlab</a>', '<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_e_description/urdf/ur3e_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR5</td><td>none</td><td>178</td><td>['<a href="urdf_files/matlab/ur_description/urdf/universalUR5.urdf">matlab</a>', '<a href="urdf_files/random/robot-assets/ur5/ur5_gripper.urdf">random</a>', '<a href="urdf_files/robotics-toolbox/xacro_generated/ur_description/urdf/ur5.urdf">robotics-toolbox</a>', '<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_description/urdf/ur5_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR5e</td><td>none</td><td>179</td><td>['<a href="urdf_files/matlab/ur_e_description/urdf/universalUR5e.urdf">matlab</a>', '<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_e_description/urdf/ur5e_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>VG10 gripper</td><td>none</td><td>180</td><td>['<a href="urdf_files/random/xacro_generated/osaka_university_onrobot/onrobot_vg10_visualization/urdf/onrobot_vg10_model.urdf">random</a>']</td><td>end effector</td></tr>
<tr><td>VGC10 gripper - 1 cup model</td><td>none</td><td>181</td><td>['<a href="urdf_files/random/xacro_generated/osaka_university_onrobot/onrobot_vgc10_visualization/urdf/onrobot_vgc10_1cup_model.urdf">random</a>']</td><td>end effector</td></tr>
<tr><td>VGC10 gripper - 4 cups model</td><td>none</td><td>182</td><td>['<a href="urdf_files/random/xacro_generated/osaka_university_onrobot/onrobot_vgc10_visualization/urdf/onrobot_vgc10_4cups_model.urdf">random</a>']</td><td>end effector</td></tr>
<tr><td>Valkyrie</td><td>none</td><td>183</td><td>['<a href="urdf_files/matlab/valkyrie/urdf/urdf/valkyrie.urdf">matlab</a>', '<a href="urdf_files/random/robot-assets/val_description/model/robots/forearm_left.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/forearm_right.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/imu_test.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/test_bench.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_A.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_A_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_B.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_B_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_C.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_C_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_D.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_D_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_sim.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_sim_angled_legj1s.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_sim_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/random/robot-assets/val_description/model/robots/valkyrie_sim_gazebo_sync.urdf">random</a>', '<a href="urdf_files/robotics-toolbox/val_description/model/robots/forearm_left.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/forearm_right.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/imu_test.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/test_bench.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_A.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_A_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_B.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_B_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_C.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_C_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_D.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_D_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_sim.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_sim_angled_legj1s.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_sim_arm_mass_sims.urdf\'), WindowsPath(\'urdf_files/robotics-toolbox/val_description/model/robots/valkyrie_sim_gazebo_sync.urdf">robotics-toolbox</a>']</td><td>humanoid robot</td></tr>
<tr><td>ViperX-300</td><td>none</td><td>184</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/vx300.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>ViperX-300s</td><td>none</td><td>185</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/vx300s.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>WidowX-200</td><td>none</td><td>186</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/wx200.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>WidowX-250</td><td>none</td><td>187</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/wx250.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>WidowX-250s</td><td>none</td><td>188</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/interbotix_descriptions/urdf/wx250s.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>YuMi</td><td>none</td><td>189</td><td>['<a href="urdf_files/matlab/yumi_description/urdf/abbYuMi.urdf">matlab</a>', '<a href="urdf_files/random/robot-assets/yumi/yumi.urdf">random</a>', '<a href="urdf_files/robotics-toolbox/yumi_description/urdf/yumi.urdf">robotics-toolbox</a>']</td><td>dual arm robot</td></tr>
<tr><td>3F gripper</td><td>articulated</td><td>190</td><td>['<a href="urdf_files/drake/atlas/urdf/robotiq_simple.urdf">drake</a>', '<a href="urdf_files/ros-industrial/robotiq/robotiq_3f_gripper_visualization/cfg/robotiq-3f-gripper_articulated.urdf">ros-industrial</a>']</td><td>end effector</td></tr>
<tr><td>3F gripper</td><td>tendons</td><td>191</td><td>['<a href="urdf_files/drake/atlas/urdf/robotiq_tendons.urdf">drake</a>']</td><td>end effector</td></tr>
<tr><td>Atlas</td><td>convex hull</td><td>192</td><td>['<a href="urdf_files/drake/atlas/urdf/atlas_convex_hull.urdf">drake</a>']</td><td>humanoid robot</td></tr>
<tr><td>Atlas</td><td>minimal contact</td><td>193</td><td>['<a href="urdf_files/drake/atlas/urdf/atlas_minimal_contact.urdf">drake</a>']</td><td>humanoid robot</td></tr>
<tr><td>Dual kuka lbr iiwa 14</td><td>polytope collision</td><td>194</td><td>['<a href="urdf_files/drake/iiwa_description/urdf/dual_iiwa14_polytope_collision.urdf">drake</a>']</td><td>dual arm robot</td></tr>
<tr><td>Fetch</td><td>Camera</td><td>195</td><td>['<a href="urdf_files/robotics-toolbox/fetch_description/robots/fetch_camera.urdf">robotics-toolbox</a>']</td><td>mobile manipulator</td></tr>
<tr><td>Franka Panda</td><td>Frankie</td><td>196</td><td>['<a href="urdf_files/robotics-toolbox/xacro_generated/franka_description/robots/frankie.urdf">robotics-toolbox</a>']</td><td>robotic arm</td></tr>
<tr><td>IRB6640</td><td>185 280</td><td>197</td><td>['<a href="urdf_files/ros-industrial/abb/abb_irb6640_support/urdf/irb6640_185_280.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka lbr iiwa 14</td><td>spheres dense collision</td><td>198</td><td>['<a href="urdf_files/drake/iiwa_description/urdf/iiwa14_spheres_dense_collision.urdf">drake</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka lbr iiwa 14</td><td>spheres dense elbow collision</td><td>199</td><td>['<a href="urdf_files/drake/iiwa_description/urdf/iiwa14_spheres_dense_elbow_collision.urdf">drake</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka lbr iiwa 14</td><td>polytope collision</td><td>200</td><td>['<a href="urdf_files/drake/iiwa_description/urdf/iiwa14_polytope_collision.urdf">drake</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka lbr iiwa 14</td><td>no collision</td><td>201</td><td>['<a href="urdf_files/drake/iiwa_description/urdf/iiwa14_no_collision.urdf">drake</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka lbr iiwa 14</td><td>spheres collision</td><td>202</td><td>['<a href="urdf_files/drake/iiwa_description/urdf/iiwa14_spheres_collision.urdf">drake</a>']</td><td>robotic arm</td></tr>
<tr><td>Kuka lbr iiwa 14</td><td>primitive collision</td><td>203</td><td>['<a href="urdf_files/drake/iiwa_description/urdf/iiwa14_primitive_collision.urdf">drake</a>']</td><td>robotic arm</td></tr>
<tr><td>LWA 4P</td><td>extended</td><td>204</td><td>['<a href="urdf_files/random/xacro_generated/schunk_modular_robotics/schunk_description/urdf/schunk_lwa4p_extended.urdf">random</a>']</td><td>robotic arm</td></tr>
<tr><td>Open Manipulator</td><td>robot</td><td>205</td><td>['<a href="urdf_files/oems/xacro_generated/open-manipulator_robotis/open_manipulator_description/urdf/open_manipulator_robot.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Pioneer LX</td><td>Devil</td><td>206</td><td>['<a href="urdf_files/oems/pioneer_adept_mobile_robots/description/urdf/pioneer-lx-devil.urdf">oems</a>']</td><td>robotic arm</td></tr>
<tr><td>Planar Kuka lbr iiwa 14</td><td>spheres dense elbow collision</td><td>207</td><td>['<a href="urdf_files/drake/iiwa_description/urdf/planar_iiwa14_spheres_dense_elbow_collision.urdf">drake</a>']</td><td>robotic arm</td></tr>
<tr><td>Turtlebot 3 Burger</td><td>for autorace 2020</td><td>208</td><td>['<a href="urdf_files/oems/xacro_generated/turtlebot3_robotis/turtlebot3_description/urdf/turtlebot3_burger_for_autorace_2020.urdf">oems</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 Burger</td><td>for autorace</td><td>209</td><td>['<a href="urdf_files/oems/xacro_generated/turtlebot3_robotis/turtlebot3_description/urdf/turtlebot3_burger_for_autorace.urdf">oems</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 Waffle</td><td>for Open Manipulator</td><td>210</td><td>['<a href="urdf_files/oems/xacro_generated/turtlebot3_robotis/turtlebot3_description/urdf/turtlebot3_waffle_for_open_manipulator.urdf">oems</a>']</td><td>mobile robot</td></tr>
<tr><td>Turtlebot 3 Waffle Pi</td><td>for Open Manipulator</td><td>211</td><td>['<a href="urdf_files/oems/xacro_generated/turtlebot3_robotis/turtlebot3_description/urdf/turtlebot3_waffle_pi_for_open_manipulator.urdf">oems</a>']</td><td>mobile robot</td></tr>
<tr><td>UR10</td><td>joint limited</td><td>212</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_description/urdf/ur10_joint_limited_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR10e</td><td>joint limited</td><td>213</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_e_description/urdf/ur10e_joint_limited_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR3</td><td>joint limited</td><td>214</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_description/urdf/ur3_joint_limited_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR3e</td><td>joint limited</td><td>215</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_e_description/urdf/ur3e_joint_limited_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR5</td><td>joint limited</td><td>216</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_description/urdf/ur5_joint_limited_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>UR5e</td><td>joint limited</td><td>217</td><td>['<a href="urdf_files/ros-industrial/xacro_generated/universal_robots/ur_e_description/urdf/ur5e_joint_limited_robot.urdf">ros-industrial</a>']</td><td>robotic arm</td></tr>
<tr><td>unknown</td><td>none</td><td>218</td><td>['<a href="urdf_files/random/robot-assets/kinova/kinova.urdf">random</a>']</td><td>unknown</td></tr>
</tbody>
</table>

### Source and Meta Information
Source and meta information files describe the source of the URDF Collection, a link to the source origin, name of the robot, manufacturer, and whether or not the file was manually xacro generated.

### Obtaining Analysis Results
The following table shows the information, which scripts to generate the information, and the resulting CSV file that contains the results.

<table>
    <tr>
        <td><b>Information</b></td>
        <td><b>Script (.py)</b></td>
        <td><b>Results CSV</b></td>
    </tr>
    <tr>
        <td>Sources and URDF files</td>
        <td><tt><a href="scripts/extract_dataset_information.py">extract_dataset_information</a></tt></td>
        <td><em>dataset_sources_n_robots</em></td>
    </tr>
    <tr>
        <td>Robot types</td>
        <td><tt><a href="scripts/extract_dataset_information.py">extract_dataset_information</a></tt></td>
        <td><em>types_information</em></td>
    </tr>
    <tr>
        <td>Manufacturers</td>
        <td><tt><a href="scripts/extract_dataset_information.py">extract_dataset_information</a></tt></td>
        <td><em>manufacturers_information</em></td>
    </tr>
    <tr>
        <td>Common folder structures</td>
        <td>Manual process</td>
        <td><em>folder_structure_information</em></td>
    </tr>
    <tr>
        <td>Source xacro generated</td>
        <td><tt><a href="scripts/extract_xacro_information.py">extract_xacro_information</a></tt></td>
        <td><em>source_xacro_information</em></td>
    </tr>
    <tr>
        <td>Manufacturer xacro generated</td>
        <td><tt><a href="scripts/extract_xacro_information.py">extract_xacro_information</a></tt></td>
        <td><em>manufacturer_xacro_information</em></td>
    </tr>
    <tr>
        <td>Duplicate robots</td>
        <td><tt><a href="scripts/extract_duplicates_information.py">extract_duplicates_information</a></tt></td>
        <td><em>duplicates_parsing_information</em></td>
    </tr>
    <tr>
        <td>Identical files</td>
        <td><tt><a href="scripts/extract_fdupe_information.py">extract_fdupe_information</a></tt></td>
        <td><em>fdupe_duplicates_res_EXT</em></td>
    </tr>
    <tr>
        <td>URDF parsing errors</td>
        <td><tt><a href="scripts/extract_ROS_parsing_issues.py">extract_ROS_parsing_issues</a></tt></td>
        <td><em>ros_parsing_errors</em></td>
    </tr>
    <tr>
        <td>URDF parsing warnings</td>
        <td><tt><a href="scripts/extract_ROS_parsing_issues.py">extract_ROS_parsing_issues</a></tt></td>
        <td><em>ros_parsing_warnings</em></td>
    </tr>
    <tr>
        <td>CAD file types</td>
        <td><tt><a href="scripts/extract_cad_information.py">extract_cad_information</a></tt></td>
        <td><em>mesh_analysis_results_SOURCE</em></td>
    </tr>
    <tr>
        <td>Joint and link count</td>
        <td><tt><a href="scripts/get_model_structure_information.py">get_model_structure_information</a></tt></td>
        <td><em>robot_type_model_information</em></td>
    </tr>
    <tr>
        <td>Word count in names of joints and links</td>
        <td><tt><a href="scripts/get_model_structure_information.py">get_model_structure_information</a></tt></td>
        <td><em>source_model_name_information</em></td>
    </tr>
</table>


## Creating the dataset

"variants" was defined by looking at the urdf file names and using them to define the variants of a robot.
An example of how a variant was defined,
drake/atlas/urdf has both 'atlas_convex_hull.urdf' and 'atlas_minimal_contact.urdf', and as this is the exact same physical robot, but with modifications to the urdf file, we have defined them as variants of the robot.
If there are robots such as ros-industrial/xacro_generated/abb/abb_irb52_support/urdf/ 'irb52_7_120.urdf' and 'irb52_7_145.urdf', we do not define them as different variants, as they are original robots with different characteristics, and have nothing to do with their urdf implementation.

<!-- "Variants" are defined by a robot with various features, e.g. the same robot but with extended or different features, this could be the payload, workspace, force, etc.
An example of this is the
If there are robots such as ros-industrial/xacro_generated/abb/abb_irb52_support/urdf/ 'irb52_7_120.urdf' and 'irb52_7_145.urdf' they are defined as robot: 'irb52 7' with the modifications '120' and '145'.

Would the drake/allegro_hand_description/urdf/ be a modification or variation -->

### Contributing
Create a pull request with the URDF Collection or source.



### Other

We are not sure if the names of the following robots are correct:
* Frankie from robotics-toolbox
* ViperX-300S from robotics-toolbox
* Jaco Jxxxxxxx from robotics-toolbox, matlab, oems
* Kinova Gen3 V12 from matlab

