import Image from 'next/image';
import React, { useState, useEffect, useRef, useCallback } from 'react';
import LoginLinks from './loginLinks';
import { useDispatch } from 'react-redux';
import { signUpAction } from '../../reducers/user';
import useInput from '../../hooks/useInput';
import { useSelector } from 'react-redux';
import FontTitle from '../font/fontTitle';
import TopNav from './topnav';
import LoginForm from './loginform';

export default function LoginNavbar() {

  const [id, onChangeId] = useInput('');
  const [nick, onChangeNick] = useInput('');
  const [password, onChangePassword] = useInput('');
  const dispatch = useDispatch();
  const isLoggedIn  = useSelector((state) => state.user.isLoggedIn);

  const onSubmit = useCallback(() => {
    console.log("er")
    dispatch(signUpAction({ id, password, nick, }));
  }, [password]);

  return (
    <div>
      <TopNav/>
      <FontTitle marginTop="mt-8" textSize="text-3xl" />
      <LoginForm onSubmit={onSubmit}/>
      <LoginLinks />
    </div>
  );
}