<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class LoginController extends Controller
{

    public function __construct()
    {
        $this->middleware(['guest']);
    }

    public function index(){
        //dd('LoginINdex');
        return view('auth.login');
    }
    public function store(Request $request){
        //dd('ok');
        $this->validate( $request,[
            'email'=>'required|email',
            'password'=>'required',
        ]);
        //auth()->attempt($request->only('email','password'));
        
        if(!auth()->attempt($request->only('email','password'),
        $request->remember)){
            return back()->with('status','Invalid login details');
        }
        
        return redirect()->route('dashboard');
    }
}
