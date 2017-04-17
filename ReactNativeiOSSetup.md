# React Native iOS Server Setup
Last update: 2017/04/17

- https://facebook.github.io/react-native/docs/getting-started.html
    - 選iOS, MacOS，按照步驟安裝
    - 然後再選Android, MacOS，按照步驟安裝

- react-native init albums
- cd albums
- npm install --save-dev eslint-config-rallycoding
- 安裝VSCode
- 到VSCode的擴充功能 安裝ESlint

- React Native @ VSCode 開發相關安裝
  - https://medium.com/react-native-training/vscode-for-react-native-526ec4a368ce
    - 安裝完Section 1: Fundamentals

  - https://github.com/Microsoft/vscode-react-native
    - React Native外掛使用說明

- Android part

Add the following lines to your ~/.profile (or equivalent) config file:

export ANDROID_HOME=${HOME}/Library/Android/sdk
export PATH=${PATH}:${ANDROID_HOME}/tools
export PATH=${PATH}:${ANDROID_HOME}/platform-tools
