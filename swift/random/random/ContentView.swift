//
//  ContentView.swift
//  random
//
//  Created by 안재민 on 4/1/25.
//

import SwiftUI

struct ContentView: View {
    @State private var name: String = ""

    var body: some View {
        VStack(spacing: 20) {
            Text("자리 배치표")
                .font(.title)

            TextField("이름을 입력하세요", text: $name)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button("확인") {
                print("입력한 이름: \(name)")
            }

            Spacer()
        }
        .padding()
        .frame(width: 300, height: 200)
    }
}

@main
struct SeatApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}


#Preview {
    ContentView()
}
