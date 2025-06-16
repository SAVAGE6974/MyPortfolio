//
//  ContentView.swift
//  unknowntitle
//
//  Created by 안재민 on 3/28/25.
//

//import SwiftUI
//
//struct ContentView: View {
//    @State private var isTapped = false
//    
//    var body: some View {
//        GeometryReader { geometry in
//            ZStack {
//                VStack {
//                    Spacer()
//                    RoundedRectangle(cornerRadius: 25)
//                        .fill(Color.gray)
//                        .frame(width: 300, height: isTapped ? 150 : 100)
//                        .shadow(radius: 4)
//                        .onTapGesture {
//                            withAnimation {
//                                isTapped.toggle()
//                            }
//                        }
//                }
//                .frame(maxWidth: .infinity, alignment: .bottom)
//                
//                Text("오늘의 기분은 어떤가요?")
//                    .font(.BMEuljiro10yearslater)
//                    .foregroundColor(.white)
//                    .multilineTextAlignment(.center)
//                    .position(x: geometry.size.width * 0.5, y: geometry.size.height * 0.13)
//                
//                Text("Learn Mack Play. Welecom to LMP")
//                    .font(.BMEuljiro10yearslater)
//                    .font(.largeTitle)
//                    .position(x: geometry.size.width * 0.5, y: geometry.size.height * 0.03)
//            }
//            
//        }
//    }
//}
//
//struct ContentView_Previews: PreviewProvider {
//    static var previews: some View {
//        ContentView()
//    }
//}

import SwiftUI

struct ContentView: View {
    @State private var isTapped = false
    
    var body: some View {
        GeometryReader { geometry in
            ZStack {
                VStack {
                    Spacer()  // 위쪽에 공간을 확보하고, 아래쪽에만 사각형이 커지도록
                    RoundedRectangle(cornerRadius: 25)
                        .fill(Color.gray)
                        .frame(width: 300, height: isTapped ? 150 : 100)  // 높이만 변경
                        .shadow(radius: 4)
                        .onTapGesture {
                            withAnimation {
                                isTapped.toggle() // 클릭 시 높이 변경
                            }
                        }
                }
                .frame(maxWidth: .infinity, alignment: .bottom)  // 아래쪽에 고정
                
                // 텍스트는 고정된 위치에 배치
                Text("오늘의 기분은 어떤가요?")
                    .font(.system(size: 20))
                    .foregroundColor(.white)
                    .multilineTextAlignment(.center)
                    .position(x: geometry.size.width * 0.5, y: geometry.size.height * 0.13)
                
                // 상단 텍스트
                Text("Learn Mack Play. Welcome to LMP")
                    .font(.system(size: 30))
                    .font(.largeTitle)
                    .position(x: geometry.size.width * 0.5, y: geometry.size.height * 0.03)
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
