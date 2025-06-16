//
//  ContentView.swift
//  swift01
//
//  Created by 안재민 on 3/29/25.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Level-up My Plan, welcome to LMP")
                .font(.custom("Apple SD Gothic Neo", size: 23).bold())
                .position(x: 190, y: 0)
            ZStack{
                RoundedRectangle(cornerRadius: 20)
                    .frame(width: 300, height: 100)
                    .foregroundColor(.black)
                
                Text("오늘은 어떤 공부를 할까요?")
                    .font(.custom("Apple SD Gothic Neo", size: 20).bold())
                    .foregroundColor(.white)
            }
            .position(x: 190, y: -160)
            
            ZStack{
                RoundedRectangle(cornerRadius: 20)
                    .frame(width: 300, height: 100)
                    .foregroundColor(.black)
                
                Text("🔹공부하기")
                    .font(.custom("Apple SD Gothic Neo", size: 20).bold())
                    .foregroundColor(.white)
            }
            .position(x: 190, y: -180)
            
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
